# _*_ coding: utf-8 _*_
"""Validators for ``pydantic`` Custom DataType"""
import importlib
import typing
from pathlib import Path
from typing import Union

from pydantic.class_validators import make_generic_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.types import StrBytes
from pydantic.utils import ROOT_KEY

from fhir.resources.core.fhirabstractmodel import FHIRAbstractModel

if typing.TYPE_CHECKING:
    from pydantic import BaseModel

__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"

MODEL_CLASSES = {
    "FHIRPrimitiveExtension": (None, ".fhirprimitiveextension"),
    "Account": (None, ".account"),
    "AccountBalance": (None, ".account"),
    "AccountCoverage": (None, ".account"),
    "AccountDiagnosis": (None, ".account"),
    "AccountGuarantor": (None, ".account"),
    "AccountProcedure": (None, ".account"),
    "AccountRelatedAccount": (None, ".account"),
    "ActivityDefinition": (None, ".activitydefinition"),
    "ActivityDefinitionDynamicValue": (None, ".activitydefinition"),
    "ActivityDefinitionParticipant": (None, ".activitydefinition"),
    "ActorDefinition": (None, ".actordefinition"),
    "Address": (None, ".address"),
    "AdministrableProductDefinition": (None, ".administrableproductdefinition"),
    "AdministrableProductDefinitionProperty": (None, ".administrableproductdefinition"),
    "AdministrableProductDefinitionRouteOfAdministration": (
        None,
        ".administrableproductdefinition",
    ),
    "AdministrableProductDefinitionRouteOfAdministrationTargetSpecies": (
        None,
        ".administrableproductdefinition",
    ),
    "AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod": (
        None,
        ".administrableproductdefinition",
    ),
    "AdverseEvent": (None, ".adverseevent"),
    "AdverseEventContributingFactor": (None, ".adverseevent"),
    "AdverseEventMitigatingAction": (None, ".adverseevent"),
    "AdverseEventParticipant": (None, ".adverseevent"),
    "AdverseEventPreventiveAction": (None, ".adverseevent"),
    "AdverseEventSupportingInfo": (None, ".adverseevent"),
    "AdverseEventSuspectEntity": (None, ".adverseevent"),
    "AdverseEventSuspectEntityCausality": (None, ".adverseevent"),
    "Age": (None, ".age"),
    "AllergyIntolerance": (None, ".allergyintolerance"),
    "AllergyIntoleranceParticipant": (None, ".allergyintolerance"),
    "AllergyIntoleranceReaction": (None, ".allergyintolerance"),
    "Annotation": (None, ".annotation"),
    "Appointment": (None, ".appointment"),
    "AppointmentParticipant": (None, ".appointment"),
    "AppointmentRecurrenceTemplate": (None, ".appointment"),
    "AppointmentRecurrenceTemplateMonthlyTemplate": (None, ".appointment"),
    "AppointmentRecurrenceTemplateWeeklyTemplate": (None, ".appointment"),
    "AppointmentRecurrenceTemplateYearlyTemplate": (None, ".appointment"),
    "AppointmentResponse": (None, ".appointmentresponse"),
    "ArtifactAssessment": (None, ".artifactassessment"),
    "ArtifactAssessmentContent": (None, ".artifactassessment"),
    "Attachment": (None, ".attachment"),
    "AuditEvent": (None, ".auditevent"),
    "AuditEventAgent": (None, ".auditevent"),
    "AuditEventEntity": (None, ".auditevent"),
    "AuditEventEntityDetail": (None, ".auditevent"),
    "AuditEventOutcome": (None, ".auditevent"),
    "AuditEventSource": (None, ".auditevent"),
    "Availability": (None, ".availability"),
    "AvailabilityAvailableTime": (None, ".availability"),
    "AvailabilityNotAvailableTime": (None, ".availability"),
    "BackboneElement": (None, ".backboneelement"),
    "BackboneType": (None, ".backbonetype"),
    "Base": (None, ".base"),
    "Basic": (None, ".basic"),
    "Binary": (None, ".binary"),
    "BiologicallyDerivedProduct": (None, ".biologicallyderivedproduct"),
    "BiologicallyDerivedProductCollection": (None, ".biologicallyderivedproduct"),
    "BiologicallyDerivedProductDispense": (None, ".biologicallyderivedproductdispense"),
    "BiologicallyDerivedProductDispensePerformer": (
        None,
        ".biologicallyderivedproductdispense",
    ),
    "BiologicallyDerivedProductProperty": (None, ".biologicallyderivedproduct"),
    "BodyStructure": (None, ".bodystructure"),
    "BodyStructureIncludedStructure": (None, ".bodystructure"),
    "BodyStructureIncludedStructureBodyLandmarkOrientation": (None, ".bodystructure"),
    "BodyStructureIncludedStructureBodyLandmarkOrientationDistanceFromLandmark": (
        None,
        ".bodystructure",
    ),
    "Bundle": (None, ".bundle"),
    "BundleEntry": (None, ".bundle"),
    "BundleEntryRequest": (None, ".bundle"),
    "BundleEntryResponse": (None, ".bundle"),
    "BundleEntrySearch": (None, ".bundle"),
    "BundleLink": (None, ".bundle"),
    "CanonicalResource": (None, ".canonicalresource"),
    "CapabilityStatement": (None, ".capabilitystatement"),
    "CapabilityStatementDocument": (None, ".capabilitystatement"),
    "CapabilityStatementImplementation": (None, ".capabilitystatement"),
    "CapabilityStatementMessaging": (None, ".capabilitystatement"),
    "CapabilityStatementMessagingEndpoint": (None, ".capabilitystatement"),
    "CapabilityStatementMessagingSupportedMessage": (None, ".capabilitystatement"),
    "CapabilityStatementRest": (None, ".capabilitystatement"),
    "CapabilityStatementRestInteraction": (None, ".capabilitystatement"),
    "CapabilityStatementRestResource": (None, ".capabilitystatement"),
    "CapabilityStatementRestResourceInteraction": (None, ".capabilitystatement"),
    "CapabilityStatementRestResourceOperation": (None, ".capabilitystatement"),
    "CapabilityStatementRestResourceSearchParam": (None, ".capabilitystatement"),
    "CapabilityStatementRestSecurity": (None, ".capabilitystatement"),
    "CapabilityStatementSoftware": (None, ".capabilitystatement"),
    "CarePlan": (None, ".careplan"),
    "CarePlanActivity": (None, ".careplan"),
    "CareTeam": (None, ".careteam"),
    "CareTeamParticipant": (None, ".careteam"),
    "ChargeItem": (None, ".chargeitem"),
    "ChargeItemDefinition": (None, ".chargeitemdefinition"),
    "ChargeItemDefinitionApplicability": (None, ".chargeitemdefinition"),
    "ChargeItemDefinitionPropertyGroup": (None, ".chargeitemdefinition"),
    "ChargeItemPerformer": (None, ".chargeitem"),
    "Citation": (None, ".citation"),
    "CitationCitedArtifact": (None, ".citation"),
    "CitationCitedArtifactAbstract": (None, ".citation"),
    "CitationCitedArtifactClassification": (None, ".citation"),
    "CitationCitedArtifactContributorship": (None, ".citation"),
    "CitationCitedArtifactContributorshipEntry": (None, ".citation"),
    "CitationCitedArtifactContributorshipEntryContributionInstance": (
        None,
        ".citation",
    ),
    "CitationCitedArtifactContributorshipSummary": (None, ".citation"),
    "CitationCitedArtifactPart": (None, ".citation"),
    "CitationCitedArtifactPublicationForm": (None, ".citation"),
    "CitationCitedArtifactPublicationFormPublishedIn": (None, ".citation"),
    "CitationCitedArtifactRelatesTo": (None, ".citation"),
    "CitationCitedArtifactStatusDate": (None, ".citation"),
    "CitationCitedArtifactTitle": (None, ".citation"),
    "CitationCitedArtifactVersion": (None, ".citation"),
    "CitationCitedArtifactWebLocation": (None, ".citation"),
    "CitationClassification": (None, ".citation"),
    "CitationStatusDate": (None, ".citation"),
    "CitationSummary": (None, ".citation"),
    "Claim": (None, ".claim"),
    "ClaimAccident": (None, ".claim"),
    "ClaimCareTeam": (None, ".claim"),
    "ClaimDiagnosis": (None, ".claim"),
    "ClaimEvent": (None, ".claim"),
    "ClaimInsurance": (None, ".claim"),
    "ClaimItem": (None, ".claim"),
    "ClaimItemBodySite": (None, ".claim"),
    "ClaimItemDetail": (None, ".claim"),
    "ClaimItemDetailSubDetail": (None, ".claim"),
    "ClaimPayee": (None, ".claim"),
    "ClaimProcedure": (None, ".claim"),
    "ClaimRelated": (None, ".claim"),
    "ClaimResponse": (None, ".claimresponse"),
    "ClaimResponseAddItem": (None, ".claimresponse"),
    "ClaimResponseAddItemBodySite": (None, ".claimresponse"),
    "ClaimResponseAddItemDetail": (None, ".claimresponse"),
    "ClaimResponseAddItemDetailSubDetail": (None, ".claimresponse"),
    "ClaimResponseError": (None, ".claimresponse"),
    "ClaimResponseEvent": (None, ".claimresponse"),
    "ClaimResponseInsurance": (None, ".claimresponse"),
    "ClaimResponseItem": (None, ".claimresponse"),
    "ClaimResponseItemAdjudication": (None, ".claimresponse"),
    "ClaimResponseItemDetail": (None, ".claimresponse"),
    "ClaimResponseItemDetailSubDetail": (None, ".claimresponse"),
    "ClaimResponseItemReviewOutcome": (None, ".claimresponse"),
    "ClaimResponsePayment": (None, ".claimresponse"),
    "ClaimResponseProcessNote": (None, ".claimresponse"),
    "ClaimResponseTotal": (None, ".claimresponse"),
    "ClaimSupportingInfo": (None, ".claim"),
    "ClinicalImpression": (None, ".clinicalimpression"),
    "ClinicalImpressionFinding": (None, ".clinicalimpression"),
    "ClinicalUseDefinition": (None, ".clinicalusedefinition"),
    "ClinicalUseDefinitionContraindication": (None, ".clinicalusedefinition"),
    "ClinicalUseDefinitionContraindicationOtherTherapy": (
        None,
        ".clinicalusedefinition",
    ),
    "ClinicalUseDefinitionIndication": (None, ".clinicalusedefinition"),
    "ClinicalUseDefinitionInteraction": (None, ".clinicalusedefinition"),
    "ClinicalUseDefinitionInteractionInteractant": (None, ".clinicalusedefinition"),
    "ClinicalUseDefinitionUndesirableEffect": (None, ".clinicalusedefinition"),
    "ClinicalUseDefinitionWarning": (None, ".clinicalusedefinition"),
    "CodeSystem": (None, ".codesystem"),
    "CodeSystemConcept": (None, ".codesystem"),
    "CodeSystemConceptDesignation": (None, ".codesystem"),
    "CodeSystemConceptProperty": (None, ".codesystem"),
    "CodeSystemFilter": (None, ".codesystem"),
    "CodeSystemProperty": (None, ".codesystem"),
    "CodeableConcept": (None, ".codeableconcept"),
    "CodeableReference": (None, ".codeablereference"),
    "Coding": (None, ".coding"),
    "Communication": (None, ".communication"),
    "CommunicationPayload": (None, ".communication"),
    "CommunicationRequest": (None, ".communicationrequest"),
    "CommunicationRequestPayload": (None, ".communicationrequest"),
    "CompartmentDefinition": (None, ".compartmentdefinition"),
    "CompartmentDefinitionResource": (None, ".compartmentdefinition"),
    "Composition": (None, ".composition"),
    "CompositionAttester": (None, ".composition"),
    "CompositionEvent": (None, ".composition"),
    "CompositionSection": (None, ".composition"),
    "ConceptMap": (None, ".conceptmap"),
    "ConceptMapAdditionalAttribute": (None, ".conceptmap"),
    "ConceptMapGroup": (None, ".conceptmap"),
    "ConceptMapGroupElement": (None, ".conceptmap"),
    "ConceptMapGroupElementTarget": (None, ".conceptmap"),
    "ConceptMapGroupElementTargetDependsOn": (None, ".conceptmap"),
    "ConceptMapGroupElementTargetProperty": (None, ".conceptmap"),
    "ConceptMapGroupUnmapped": (None, ".conceptmap"),
    "ConceptMapProperty": (None, ".conceptmap"),
    "Condition": (None, ".condition"),
    "ConditionDefinition": (None, ".conditiondefinition"),
    "ConditionDefinitionMedication": (None, ".conditiondefinition"),
    "ConditionDefinitionObservation": (None, ".conditiondefinition"),
    "ConditionDefinitionPlan": (None, ".conditiondefinition"),
    "ConditionDefinitionPrecondition": (None, ".conditiondefinition"),
    "ConditionDefinitionQuestionnaire": (None, ".conditiondefinition"),
    "ConditionParticipant": (None, ".condition"),
    "ConditionStage": (None, ".condition"),
    "Consent": (None, ".consent"),
    "ConsentPolicyBasis": (None, ".consent"),
    "ConsentProvision": (None, ".consent"),
    "ConsentProvisionActor": (None, ".consent"),
    "ConsentProvisionData": (None, ".consent"),
    "ConsentVerification": (None, ".consent"),
    "ContactDetail": (None, ".contactdetail"),
    "ContactPoint": (None, ".contactpoint"),
    "Contract": (None, ".contract"),
    "ContractContentDefinition": (None, ".contract"),
    "ContractFriendly": (None, ".contract"),
    "ContractLegal": (None, ".contract"),
    "ContractRule": (None, ".contract"),
    "ContractSigner": (None, ".contract"),
    "ContractTerm": (None, ".contract"),
    "ContractTermAction": (None, ".contract"),
    "ContractTermActionSubject": (None, ".contract"),
    "ContractTermAsset": (None, ".contract"),
    "ContractTermAssetContext": (None, ".contract"),
    "ContractTermAssetValuedItem": (None, ".contract"),
    "ContractTermOffer": (None, ".contract"),
    "ContractTermOfferAnswer": (None, ".contract"),
    "ContractTermOfferParty": (None, ".contract"),
    "ContractTermSecurityLabel": (None, ".contract"),
    "Contributor": (None, ".contributor"),
    "Count": (None, ".count"),
    "Coverage": (None, ".coverage"),
    "CoverageClass": (None, ".coverage"),
    "CoverageCostToBeneficiary": (None, ".coverage"),
    "CoverageCostToBeneficiaryException": (None, ".coverage"),
    "CoverageEligibilityRequest": (None, ".coverageeligibilityrequest"),
    "CoverageEligibilityRequestEvent": (None, ".coverageeligibilityrequest"),
    "CoverageEligibilityRequestInsurance": (None, ".coverageeligibilityrequest"),
    "CoverageEligibilityRequestItem": (None, ".coverageeligibilityrequest"),
    "CoverageEligibilityRequestItemDiagnosis": (None, ".coverageeligibilityrequest"),
    "CoverageEligibilityRequestSupportingInfo": (None, ".coverageeligibilityrequest"),
    "CoverageEligibilityResponse": (None, ".coverageeligibilityresponse"),
    "CoverageEligibilityResponseError": (None, ".coverageeligibilityresponse"),
    "CoverageEligibilityResponseEvent": (None, ".coverageeligibilityresponse"),
    "CoverageEligibilityResponseInsurance": (None, ".coverageeligibilityresponse"),
    "CoverageEligibilityResponseInsuranceItem": (None, ".coverageeligibilityresponse"),
    "CoverageEligibilityResponseInsuranceItemBenefit": (
        None,
        ".coverageeligibilityresponse",
    ),
    "CoveragePaymentBy": (None, ".coverage"),
    "DataRequirement": (None, ".datarequirement"),
    "DataRequirementCodeFilter": (None, ".datarequirement"),
    "DataRequirementDateFilter": (None, ".datarequirement"),
    "DataRequirementSort": (None, ".datarequirement"),
    "DataRequirementValueFilter": (None, ".datarequirement"),
    "DataType": (None, ".datatype"),
    "DetectedIssue": (None, ".detectedissue"),
    "DetectedIssueEvidence": (None, ".detectedissue"),
    "DetectedIssueMitigation": (None, ".detectedissue"),
    "Device": (None, ".device"),
    "DeviceAssociation": (None, ".deviceassociation"),
    "DeviceAssociationOperation": (None, ".deviceassociation"),
    "DeviceConformsTo": (None, ".device"),
    "DeviceDefinition": (None, ".devicedefinition"),
    "DeviceDefinitionChargeItem": (None, ".devicedefinition"),
    "DeviceDefinitionClassification": (None, ".devicedefinition"),
    "DeviceDefinitionConformsTo": (None, ".devicedefinition"),
    "DeviceDefinitionCorrectiveAction": (None, ".devicedefinition"),
    "DeviceDefinitionDeviceName": (None, ".devicedefinition"),
    "DeviceDefinitionGuideline": (None, ".devicedefinition"),
    "DeviceDefinitionHasPart": (None, ".devicedefinition"),
    "DeviceDefinitionLink": (None, ".devicedefinition"),
    "DeviceDefinitionMaterial": (None, ".devicedefinition"),
    "DeviceDefinitionPackaging": (None, ".devicedefinition"),
    "DeviceDefinitionPackagingDistributor": (None, ".devicedefinition"),
    "DeviceDefinitionProperty": (None, ".devicedefinition"),
    "DeviceDefinitionRegulatoryIdentifier": (None, ".devicedefinition"),
    "DeviceDefinitionUdiDeviceIdentifier": (None, ".devicedefinition"),
    "DeviceDefinitionUdiDeviceIdentifierMarketDistribution": (
        None,
        ".devicedefinition",
    ),
    "DeviceDefinitionVersion": (None, ".devicedefinition"),
    "DeviceDispense": (None, ".devicedispense"),
    "DeviceDispensePerformer": (None, ".devicedispense"),
    "DeviceMetric": (None, ".devicemetric"),
    "DeviceMetricCalibration": (None, ".devicemetric"),
    "DeviceName": (None, ".device"),
    "DeviceProperty": (None, ".device"),
    "DeviceRequest": (None, ".devicerequest"),
    "DeviceRequestParameter": (None, ".devicerequest"),
    "DeviceUdiCarrier": (None, ".device"),
    "DeviceUsage": (None, ".deviceusage"),
    "DeviceUsageAdherence": (None, ".deviceusage"),
    "DeviceVersion": (None, ".device"),
    "DiagnosticReport": (None, ".diagnosticreport"),
    "DiagnosticReportMedia": (None, ".diagnosticreport"),
    "DiagnosticReportSupportingInfo": (None, ".diagnosticreport"),
    "Distance": (None, ".distance"),
    "DocumentReference": (None, ".documentreference"),
    "DocumentReferenceAttester": (None, ".documentreference"),
    "DocumentReferenceContent": (None, ".documentreference"),
    "DocumentReferenceContentProfile": (None, ".documentreference"),
    "DocumentReferenceRelatesTo": (None, ".documentreference"),
    "DomainResource": (None, ".domainresource"),
    "Dosage": (None, ".dosage"),
    "DosageDoseAndRate": (None, ".dosage"),
    "Duration": (None, ".duration"),
    "Element": (None, ".element"),
    "ElementDefinition": (None, ".elementdefinition"),
    "ElementDefinitionBase": (None, ".elementdefinition"),
    "ElementDefinitionBinding": (None, ".elementdefinition"),
    "ElementDefinitionBindingAdditional": (None, ".elementdefinition"),
    "ElementDefinitionConstraint": (None, ".elementdefinition"),
    "ElementDefinitionExample": (None, ".elementdefinition"),
    "ElementDefinitionMapping": (None, ".elementdefinition"),
    "ElementDefinitionSlicing": (None, ".elementdefinition"),
    "ElementDefinitionSlicingDiscriminator": (None, ".elementdefinition"),
    "ElementDefinitionType": (None, ".elementdefinition"),
    "Encounter": (None, ".encounter"),
    "EncounterAdmission": (None, ".encounter"),
    "EncounterDiagnosis": (None, ".encounter"),
    "EncounterHistory": (None, ".encounterhistory"),
    "EncounterHistoryLocation": (None, ".encounterhistory"),
    "EncounterLocation": (None, ".encounter"),
    "EncounterParticipant": (None, ".encounter"),
    "EncounterReason": (None, ".encounter"),
    "Endpoint": (None, ".endpoint"),
    "EndpointPayload": (None, ".endpoint"),
    "EnrollmentRequest": (None, ".enrollmentrequest"),
    "EnrollmentResponse": (None, ".enrollmentresponse"),
    "EpisodeOfCare": (None, ".episodeofcare"),
    "EpisodeOfCareDiagnosis": (None, ".episodeofcare"),
    "EpisodeOfCareReason": (None, ".episodeofcare"),
    "EpisodeOfCareStatusHistory": (None, ".episodeofcare"),
    "EventDefinition": (None, ".eventdefinition"),
    "Evidence": (None, ".evidence"),
    "EvidenceCertainty": (None, ".evidence"),
    "EvidenceReport": (None, ".evidencereport"),
    "EvidenceReportRelatesTo": (None, ".evidencereport"),
    "EvidenceReportRelatesToTarget": (None, ".evidencereport"),
    "EvidenceReportSection": (None, ".evidencereport"),
    "EvidenceReportSubject": (None, ".evidencereport"),
    "EvidenceReportSubjectCharacteristic": (None, ".evidencereport"),
    "EvidenceStatistic": (None, ".evidence"),
    "EvidenceStatisticAttributeEstimate": (None, ".evidence"),
    "EvidenceStatisticModelCharacteristic": (None, ".evidence"),
    "EvidenceStatisticModelCharacteristicVariable": (None, ".evidence"),
    "EvidenceStatisticSampleSize": (None, ".evidence"),
    "EvidenceVariable": (None, ".evidencevariable"),
    "EvidenceVariableCategory": (None, ".evidencevariable"),
    "EvidenceVariableCharacteristic": (None, ".evidencevariable"),
    "EvidenceVariableCharacteristicDefinitionByCombination": (
        None,
        ".evidencevariable",
    ),
    "EvidenceVariableCharacteristicDefinitionByTypeAndValue": (
        None,
        ".evidencevariable",
    ),
    "EvidenceVariableCharacteristicTimeFromEvent": (None, ".evidencevariable"),
    "EvidenceVariableDefinition": (None, ".evidence"),
    "ExampleScenario": (None, ".examplescenario"),
    "ExampleScenarioActor": (None, ".examplescenario"),
    "ExampleScenarioInstance": (None, ".examplescenario"),
    "ExampleScenarioInstanceContainedInstance": (None, ".examplescenario"),
    "ExampleScenarioInstanceVersion": (None, ".examplescenario"),
    "ExampleScenarioProcess": (None, ".examplescenario"),
    "ExampleScenarioProcessStep": (None, ".examplescenario"),
    "ExampleScenarioProcessStepAlternative": (None, ".examplescenario"),
    "ExampleScenarioProcessStepOperation": (None, ".examplescenario"),
    "ExplanationOfBenefit": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitAccident": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitAddItem": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitAddItemBodySite": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitAddItemDetail": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitAddItemDetailSubDetail": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitBenefitBalance": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitBenefitBalanceFinancial": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitCareTeam": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitDiagnosis": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitEvent": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitInsurance": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitItem": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitItemAdjudication": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitItemBodySite": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitItemDetail": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitItemDetailSubDetail": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitItemReviewOutcome": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitPayee": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitPayment": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitProcedure": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitProcessNote": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitRelated": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitSupportingInfo": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitTotal": (None, ".explanationofbenefit"),
    "Expression": (None, ".expression"),
    "ExtendedContactDetail": (None, ".extendedcontactdetail"),
    "Extension": (None, ".extension"),
    "FamilyMemberHistory": (None, ".familymemberhistory"),
    "FamilyMemberHistoryCondition": (None, ".familymemberhistory"),
    "FamilyMemberHistoryParticipant": (None, ".familymemberhistory"),
    "FamilyMemberHistoryProcedure": (None, ".familymemberhistory"),
    "Flag": (None, ".flag"),
    "FormularyItem": (None, ".formularyitem"),
    "GenomicStudy": (None, ".genomicstudy"),
    "GenomicStudyAnalysis": (None, ".genomicstudy"),
    "GenomicStudyAnalysisDevice": (None, ".genomicstudy"),
    "GenomicStudyAnalysisInput": (None, ".genomicstudy"),
    "GenomicStudyAnalysisOutput": (None, ".genomicstudy"),
    "GenomicStudyAnalysisPerformer": (None, ".genomicstudy"),
    "Goal": (None, ".goal"),
    "GoalTarget": (None, ".goal"),
    "GraphDefinition": (None, ".graphdefinition"),
    "GraphDefinitionLink": (None, ".graphdefinition"),
    "GraphDefinitionLinkCompartment": (None, ".graphdefinition"),
    "GraphDefinitionNode": (None, ".graphdefinition"),
    "Group": (None, ".group"),
    "GroupCharacteristic": (None, ".group"),
    "GroupMember": (None, ".group"),
    "GuidanceResponse": (None, ".guidanceresponse"),
    "HealthcareService": (None, ".healthcareservice"),
    "HealthcareServiceEligibility": (None, ".healthcareservice"),
    "HumanName": (None, ".humanname"),
    "Identifier": (None, ".identifier"),
    "ImagingSelection": (None, ".imagingselection"),
    "ImagingSelectionInstance": (None, ".imagingselection"),
    "ImagingSelectionInstanceImageRegion2D": (None, ".imagingselection"),
    "ImagingSelectionInstanceImageRegion3D": (None, ".imagingselection"),
    "ImagingSelectionPerformer": (None, ".imagingselection"),
    "ImagingStudy": (None, ".imagingstudy"),
    "ImagingStudySeries": (None, ".imagingstudy"),
    "ImagingStudySeriesInstance": (None, ".imagingstudy"),
    "ImagingStudySeriesPerformer": (None, ".imagingstudy"),
    "Immunization": (None, ".immunization"),
    "ImmunizationEvaluation": (None, ".immunizationevaluation"),
    "ImmunizationPerformer": (None, ".immunization"),
    "ImmunizationProgramEligibility": (None, ".immunization"),
    "ImmunizationProtocolApplied": (None, ".immunization"),
    "ImmunizationReaction": (None, ".immunization"),
    "ImmunizationRecommendation": (None, ".immunizationrecommendation"),
    "ImmunizationRecommendationRecommendation": (None, ".immunizationrecommendation"),
    "ImmunizationRecommendationRecommendationDateCriterion": (
        None,
        ".immunizationrecommendation",
    ),
    "ImplementationGuide": (None, ".implementationguide"),
    "ImplementationGuideDefinition": (None, ".implementationguide"),
    "ImplementationGuideDefinitionGrouping": (None, ".implementationguide"),
    "ImplementationGuideDefinitionPage": (None, ".implementationguide"),
    "ImplementationGuideDefinitionParameter": (None, ".implementationguide"),
    "ImplementationGuideDefinitionResource": (None, ".implementationguide"),
    "ImplementationGuideDefinitionTemplate": (None, ".implementationguide"),
    "ImplementationGuideDependsOn": (None, ".implementationguide"),
    "ImplementationGuideGlobal": (None, ".implementationguide"),
    "ImplementationGuideManifest": (None, ".implementationguide"),
    "ImplementationGuideManifestPage": (None, ".implementationguide"),
    "ImplementationGuideManifestResource": (None, ".implementationguide"),
    "Ingredient": (None, ".ingredient"),
    "IngredientManufacturer": (None, ".ingredient"),
    "IngredientSubstance": (None, ".ingredient"),
    "IngredientSubstanceStrength": (None, ".ingredient"),
    "IngredientSubstanceStrengthReferenceStrength": (None, ".ingredient"),
    "InsurancePlan": (None, ".insuranceplan"),
    "InsurancePlanCoverage": (None, ".insuranceplan"),
    "InsurancePlanCoverageBenefit": (None, ".insuranceplan"),
    "InsurancePlanCoverageBenefitLimit": (None, ".insuranceplan"),
    "InsurancePlanPlan": (None, ".insuranceplan"),
    "InsurancePlanPlanGeneralCost": (None, ".insuranceplan"),
    "InsurancePlanPlanSpecificCost": (None, ".insuranceplan"),
    "InsurancePlanPlanSpecificCostBenefit": (None, ".insuranceplan"),
    "InsurancePlanPlanSpecificCostBenefitCost": (None, ".insuranceplan"),
    "InventoryItem": (None, ".inventoryitem"),
    "InventoryItemAssociation": (None, ".inventoryitem"),
    "InventoryItemCharacteristic": (None, ".inventoryitem"),
    "InventoryItemDescription": (None, ".inventoryitem"),
    "InventoryItemInstance": (None, ".inventoryitem"),
    "InventoryItemName": (None, ".inventoryitem"),
    "InventoryItemResponsibleOrganization": (None, ".inventoryitem"),
    "InventoryReport": (None, ".inventoryreport"),
    "InventoryReportInventoryListing": (None, ".inventoryreport"),
    "InventoryReportInventoryListingItem": (None, ".inventoryreport"),
    "Invoice": (None, ".invoice"),
    "InvoiceLineItem": (None, ".invoice"),
    "InvoiceParticipant": (None, ".invoice"),
    "Library": (None, ".library"),
    "Linkage": (None, ".linkage"),
    "LinkageItem": (None, ".linkage"),
    "List": (None, ".list"),
    "ListEntry": (None, ".list"),
    "Location": (None, ".location"),
    "LocationPosition": (None, ".location"),
    "ManufacturedItemDefinition": (None, ".manufactureditemdefinition"),
    "ManufacturedItemDefinitionComponent": (None, ".manufactureditemdefinition"),
    "ManufacturedItemDefinitionComponentConstituent": (
        None,
        ".manufactureditemdefinition",
    ),
    "ManufacturedItemDefinitionProperty": (None, ".manufactureditemdefinition"),
    "MarketingStatus": (None, ".marketingstatus"),
    "Measure": (None, ".measure"),
    "MeasureGroup": (None, ".measure"),
    "MeasureGroupPopulation": (None, ".measure"),
    "MeasureGroupStratifier": (None, ".measure"),
    "MeasureGroupStratifierComponent": (None, ".measure"),
    "MeasureReport": (None, ".measurereport"),
    "MeasureReportGroup": (None, ".measurereport"),
    "MeasureReportGroupPopulation": (None, ".measurereport"),
    "MeasureReportGroupStratifier": (None, ".measurereport"),
    "MeasureReportGroupStratifierStratum": (None, ".measurereport"),
    "MeasureReportGroupStratifierStratumComponent": (None, ".measurereport"),
    "MeasureReportGroupStratifierStratumPopulation": (None, ".measurereport"),
    "MeasureSupplementalData": (None, ".measure"),
    "MeasureTerm": (None, ".measure"),
    "Medication": (None, ".medication"),
    "MedicationAdministration": (None, ".medicationadministration"),
    "MedicationAdministrationDosage": (None, ".medicationadministration"),
    "MedicationAdministrationPerformer": (None, ".medicationadministration"),
    "MedicationBatch": (None, ".medication"),
    "MedicationDispense": (None, ".medicationdispense"),
    "MedicationDispensePerformer": (None, ".medicationdispense"),
    "MedicationDispenseSubstitution": (None, ".medicationdispense"),
    "MedicationIngredient": (None, ".medication"),
    "MedicationKnowledge": (None, ".medicationknowledge"),
    "MedicationKnowledgeCost": (None, ".medicationknowledge"),
    "MedicationKnowledgeDefinitional": (None, ".medicationknowledge"),
    "MedicationKnowledgeDefinitionalDrugCharacteristic": (None, ".medicationknowledge"),
    "MedicationKnowledgeDefinitionalIngredient": (None, ".medicationknowledge"),
    "MedicationKnowledgeIndicationGuideline": (None, ".medicationknowledge"),
    "MedicationKnowledgeIndicationGuidelineDosingGuideline": (
        None,
        ".medicationknowledge",
    ),
    "MedicationKnowledgeIndicationGuidelineDosingGuidelineDosage": (
        None,
        ".medicationknowledge",
    ),
    "MedicationKnowledgeIndicationGuidelineDosingGuidelinePatientCharacteristic": (
        None,
        ".medicationknowledge",
    ),
    "MedicationKnowledgeMedicineClassification": (None, ".medicationknowledge"),
    "MedicationKnowledgeMonitoringProgram": (None, ".medicationknowledge"),
    "MedicationKnowledgeMonograph": (None, ".medicationknowledge"),
    "MedicationKnowledgePackaging": (None, ".medicationknowledge"),
    "MedicationKnowledgeRegulatory": (None, ".medicationknowledge"),
    "MedicationKnowledgeRegulatoryMaxDispense": (None, ".medicationknowledge"),
    "MedicationKnowledgeRegulatorySubstitution": (None, ".medicationknowledge"),
    "MedicationKnowledgeRelatedMedicationKnowledge": (None, ".medicationknowledge"),
    "MedicationKnowledgeStorageGuideline": (None, ".medicationknowledge"),
    "MedicationKnowledgeStorageGuidelineEnvironmentalSetting": (
        None,
        ".medicationknowledge",
    ),
    "MedicationRequest": (None, ".medicationrequest"),
    "MedicationRequestDispenseRequest": (None, ".medicationrequest"),
    "MedicationRequestDispenseRequestInitialFill": (None, ".medicationrequest"),
    "MedicationRequestSubstitution": (None, ".medicationrequest"),
    "MedicationStatement": (None, ".medicationstatement"),
    "MedicationStatementAdherence": (None, ".medicationstatement"),
    "MedicinalProductDefinition": (None, ".medicinalproductdefinition"),
    "MedicinalProductDefinitionCharacteristic": (None, ".medicinalproductdefinition"),
    "MedicinalProductDefinitionContact": (None, ".medicinalproductdefinition"),
    "MedicinalProductDefinitionCrossReference": (None, ".medicinalproductdefinition"),
    "MedicinalProductDefinitionName": (None, ".medicinalproductdefinition"),
    "MedicinalProductDefinitionNamePart": (None, ".medicinalproductdefinition"),
    "MedicinalProductDefinitionNameUsage": (None, ".medicinalproductdefinition"),
    "MedicinalProductDefinitionOperation": (None, ".medicinalproductdefinition"),
    "MessageDefinition": (None, ".messagedefinition"),
    "MessageDefinitionAllowedResponse": (None, ".messagedefinition"),
    "MessageDefinitionFocus": (None, ".messagedefinition"),
    "MessageHeader": (None, ".messageheader"),
    "MessageHeaderDestination": (None, ".messageheader"),
    "MessageHeaderResponse": (None, ".messageheader"),
    "MessageHeaderSource": (None, ".messageheader"),
    "Meta": (None, ".meta"),
    "MetadataResource": (None, ".metadataresource"),
    "MolecularSequence": (None, ".molecularsequence"),
    "MolecularSequenceRelative": (None, ".molecularsequence"),
    "MolecularSequenceRelativeEdit": (None, ".molecularsequence"),
    "MolecularSequenceRelativeStartingSequence": (None, ".molecularsequence"),
    "MonetaryComponent": (None, ".monetarycomponent"),
    "Money": (None, ".money"),
    "NamingSystem": (None, ".namingsystem"),
    "NamingSystemUniqueId": (None, ".namingsystem"),
    "Narrative": (None, ".narrative"),
    "NutritionIntake": (None, ".nutritionintake"),
    "NutritionIntakeConsumedItem": (None, ".nutritionintake"),
    "NutritionIntakeIngredientLabel": (None, ".nutritionintake"),
    "NutritionIntakePerformer": (None, ".nutritionintake"),
    "NutritionOrder": (None, ".nutritionorder"),
    "NutritionOrderEnteralFormula": (None, ".nutritionorder"),
    "NutritionOrderEnteralFormulaAdditive": (None, ".nutritionorder"),
    "NutritionOrderEnteralFormulaAdministration": (None, ".nutritionorder"),
    "NutritionOrderEnteralFormulaAdministrationSchedule": (None, ".nutritionorder"),
    "NutritionOrderOralDiet": (None, ".nutritionorder"),
    "NutritionOrderOralDietNutrient": (None, ".nutritionorder"),
    "NutritionOrderOralDietSchedule": (None, ".nutritionorder"),
    "NutritionOrderOralDietTexture": (None, ".nutritionorder"),
    "NutritionOrderSupplement": (None, ".nutritionorder"),
    "NutritionOrderSupplementSchedule": (None, ".nutritionorder"),
    "NutritionProduct": (None, ".nutritionproduct"),
    "NutritionProductCharacteristic": (None, ".nutritionproduct"),
    "NutritionProductIngredient": (None, ".nutritionproduct"),
    "NutritionProductInstance": (None, ".nutritionproduct"),
    "NutritionProductNutrient": (None, ".nutritionproduct"),
    "Observation": (None, ".observation"),
    "ObservationComponent": (None, ".observation"),
    "ObservationDefinition": (None, ".observationdefinition"),
    "ObservationDefinitionComponent": (None, ".observationdefinition"),
    "ObservationDefinitionQualifiedValue": (None, ".observationdefinition"),
    "ObservationReferenceRange": (None, ".observation"),
    "ObservationTriggeredBy": (None, ".observation"),
    "OperationDefinition": (None, ".operationdefinition"),
    "OperationDefinitionOverload": (None, ".operationdefinition"),
    "OperationDefinitionParameter": (None, ".operationdefinition"),
    "OperationDefinitionParameterBinding": (None, ".operationdefinition"),
    "OperationDefinitionParameterReferencedFrom": (None, ".operationdefinition"),
    "OperationOutcome": (None, ".operationoutcome"),
    "OperationOutcomeIssue": (None, ".operationoutcome"),
    "Organization": (None, ".organization"),
    "OrganizationAffiliation": (None, ".organizationaffiliation"),
    "OrganizationQualification": (None, ".organization"),
    "PackagedProductDefinition": (None, ".packagedproductdefinition"),
    "PackagedProductDefinitionLegalStatusOfSupply": (
        None,
        ".packagedproductdefinition",
    ),
    "PackagedProductDefinitionPackaging": (None, ".packagedproductdefinition"),
    "PackagedProductDefinitionPackagingContainedItem": (
        None,
        ".packagedproductdefinition",
    ),
    "PackagedProductDefinitionPackagingProperty": (None, ".packagedproductdefinition"),
    "ParameterDefinition": (None, ".parameterdefinition"),
    "Parameters": (None, ".parameters"),
    "ParametersParameter": (None, ".parameters"),
    "Patient": (None, ".patient"),
    "PatientCommunication": (None, ".patient"),
    "PatientContact": (None, ".patient"),
    "PatientLink": (None, ".patient"),
    "PaymentNotice": (None, ".paymentnotice"),
    "PaymentReconciliation": (None, ".paymentreconciliation"),
    "PaymentReconciliationAllocation": (None, ".paymentreconciliation"),
    "PaymentReconciliationProcessNote": (None, ".paymentreconciliation"),
    "Period": (None, ".period"),
    "Permission": (None, ".permission"),
    "PermissionJustification": (None, ".permission"),
    "PermissionRule": (None, ".permission"),
    "PermissionRuleActivity": (None, ".permission"),
    "PermissionRuleData": (None, ".permission"),
    "PermissionRuleDataResource": (None, ".permission"),
    "Person": (None, ".person"),
    "PersonCommunication": (None, ".person"),
    "PersonLink": (None, ".person"),
    "PlanDefinition": (None, ".plandefinition"),
    "PlanDefinitionAction": (None, ".plandefinition"),
    "PlanDefinitionActionCondition": (None, ".plandefinition"),
    "PlanDefinitionActionDynamicValue": (None, ".plandefinition"),
    "PlanDefinitionActionInput": (None, ".plandefinition"),
    "PlanDefinitionActionOutput": (None, ".plandefinition"),
    "PlanDefinitionActionParticipant": (None, ".plandefinition"),
    "PlanDefinitionActionRelatedAction": (None, ".plandefinition"),
    "PlanDefinitionActor": (None, ".plandefinition"),
    "PlanDefinitionActorOption": (None, ".plandefinition"),
    "PlanDefinitionGoal": (None, ".plandefinition"),
    "PlanDefinitionGoalTarget": (None, ".plandefinition"),
    "Practitioner": (None, ".practitioner"),
    "PractitionerCommunication": (None, ".practitioner"),
    "PractitionerQualification": (None, ".practitioner"),
    "PractitionerRole": (None, ".practitionerrole"),
    "PrimitiveType": (None, ".primitivetype"),
    "Procedure": (None, ".procedure"),
    "ProcedureFocalDevice": (None, ".procedure"),
    "ProcedurePerformer": (None, ".procedure"),
    "ProductShelfLife": (None, ".productshelflife"),
    "Provenance": (None, ".provenance"),
    "ProvenanceAgent": (None, ".provenance"),
    "ProvenanceEntity": (None, ".provenance"),
    "Quantity": (None, ".quantity"),
    "Questionnaire": (None, ".questionnaire"),
    "QuestionnaireItem": (None, ".questionnaire"),
    "QuestionnaireItemAnswerOption": (None, ".questionnaire"),
    "QuestionnaireItemEnableWhen": (None, ".questionnaire"),
    "QuestionnaireItemInitial": (None, ".questionnaire"),
    "QuestionnaireResponse": (None, ".questionnaireresponse"),
    "QuestionnaireResponseItem": (None, ".questionnaireresponse"),
    "QuestionnaireResponseItemAnswer": (None, ".questionnaireresponse"),
    "Range": (None, ".range"),
    "Ratio": (None, ".ratio"),
    "RatioRange": (None, ".ratiorange"),
    "Reference": (None, ".reference"),
    "RegulatedAuthorization": (None, ".regulatedauthorization"),
    "RegulatedAuthorizationCase": (None, ".regulatedauthorization"),
    "RelatedArtifact": (None, ".relatedartifact"),
    "RelatedPerson": (None, ".relatedperson"),
    "RelatedPersonCommunication": (None, ".relatedperson"),
    "RequestOrchestration": (None, ".requestorchestration"),
    "RequestOrchestrationAction": (None, ".requestorchestration"),
    "RequestOrchestrationActionCondition": (None, ".requestorchestration"),
    "RequestOrchestrationActionDynamicValue": (None, ".requestorchestration"),
    "RequestOrchestrationActionInput": (None, ".requestorchestration"),
    "RequestOrchestrationActionOutput": (None, ".requestorchestration"),
    "RequestOrchestrationActionParticipant": (None, ".requestorchestration"),
    "RequestOrchestrationActionRelatedAction": (None, ".requestorchestration"),
    "Requirements": (None, ".requirements"),
    "RequirementsStatement": (None, ".requirements"),
    "ResearchStudy": (None, ".researchstudy"),
    "ResearchStudyAssociatedParty": (None, ".researchstudy"),
    "ResearchStudyComparisonGroup": (None, ".researchstudy"),
    "ResearchStudyLabel": (None, ".researchstudy"),
    "ResearchStudyObjective": (None, ".researchstudy"),
    "ResearchStudyOutcomeMeasure": (None, ".researchstudy"),
    "ResearchStudyProgressStatus": (None, ".researchstudy"),
    "ResearchStudyRecruitment": (None, ".researchstudy"),
    "ResearchSubject": (None, ".researchsubject"),
    "ResearchSubjectProgress": (None, ".researchsubject"),
    "Resource": (None, ".resource"),
    "RiskAssessment": (None, ".riskassessment"),
    "RiskAssessmentPrediction": (None, ".riskassessment"),
    "SampledData": (None, ".sampleddata"),
    "Schedule": (None, ".schedule"),
    "SearchParameter": (None, ".searchparameter"),
    "SearchParameterComponent": (None, ".searchparameter"),
    "ServiceRequest": (None, ".servicerequest"),
    "ServiceRequestOrderDetail": (None, ".servicerequest"),
    "ServiceRequestOrderDetailParameter": (None, ".servicerequest"),
    "ServiceRequestPatientInstruction": (None, ".servicerequest"),
    "Signature": (None, ".signature"),
    "Slot": (None, ".slot"),
    "Specimen": (None, ".specimen"),
    "SpecimenCollection": (None, ".specimen"),
    "SpecimenContainer": (None, ".specimen"),
    "SpecimenDefinition": (None, ".specimendefinition"),
    "SpecimenDefinitionTypeTested": (None, ".specimendefinition"),
    "SpecimenDefinitionTypeTestedContainer": (None, ".specimendefinition"),
    "SpecimenDefinitionTypeTestedContainerAdditive": (None, ".specimendefinition"),
    "SpecimenDefinitionTypeTestedHandling": (None, ".specimendefinition"),
    "SpecimenFeature": (None, ".specimen"),
    "SpecimenProcessing": (None, ".specimen"),
    "StructureDefinition": (None, ".structuredefinition"),
    "StructureDefinitionContext": (None, ".structuredefinition"),
    "StructureDefinitionDifferential": (None, ".structuredefinition"),
    "StructureDefinitionMapping": (None, ".structuredefinition"),
    "StructureDefinitionSnapshot": (None, ".structuredefinition"),
    "StructureMap": (None, ".structuremap"),
    "StructureMapConst": (None, ".structuremap"),
    "StructureMapGroup": (None, ".structuremap"),
    "StructureMapGroupInput": (None, ".structuremap"),
    "StructureMapGroupRule": (None, ".structuremap"),
    "StructureMapGroupRuleDependent": (None, ".structuremap"),
    "StructureMapGroupRuleSource": (None, ".structuremap"),
    "StructureMapGroupRuleTarget": (None, ".structuremap"),
    "StructureMapGroupRuleTargetParameter": (None, ".structuremap"),
    "StructureMapStructure": (None, ".structuremap"),
    "Subscription": (None, ".subscription"),
    "SubscriptionFilterBy": (None, ".subscription"),
    "SubscriptionParameter": (None, ".subscription"),
    "SubscriptionStatus": (None, ".subscriptionstatus"),
    "SubscriptionStatusNotificationEvent": (None, ".subscriptionstatus"),
    "SubscriptionTopic": (None, ".subscriptiontopic"),
    "SubscriptionTopicCanFilterBy": (None, ".subscriptiontopic"),
    "SubscriptionTopicEventTrigger": (None, ".subscriptiontopic"),
    "SubscriptionTopicNotificationShape": (None, ".subscriptiontopic"),
    "SubscriptionTopicResourceTrigger": (None, ".subscriptiontopic"),
    "SubscriptionTopicResourceTriggerQueryCriteria": (None, ".subscriptiontopic"),
    "Substance": (None, ".substance"),
    "SubstanceDefinition": (None, ".substancedefinition"),
    "SubstanceDefinitionCharacterization": (None, ".substancedefinition"),
    "SubstanceDefinitionCode": (None, ".substancedefinition"),
    "SubstanceDefinitionMoiety": (None, ".substancedefinition"),
    "SubstanceDefinitionMolecularWeight": (None, ".substancedefinition"),
    "SubstanceDefinitionName": (None, ".substancedefinition"),
    "SubstanceDefinitionNameOfficial": (None, ".substancedefinition"),
    "SubstanceDefinitionProperty": (None, ".substancedefinition"),
    "SubstanceDefinitionRelationship": (None, ".substancedefinition"),
    "SubstanceDefinitionSourceMaterial": (None, ".substancedefinition"),
    "SubstanceDefinitionStructure": (None, ".substancedefinition"),
    "SubstanceDefinitionStructureRepresentation": (None, ".substancedefinition"),
    "SubstanceIngredient": (None, ".substance"),
    "SubstanceNucleicAcid": (None, ".substancenucleicacid"),
    "SubstanceNucleicAcidSubunit": (None, ".substancenucleicacid"),
    "SubstanceNucleicAcidSubunitLinkage": (None, ".substancenucleicacid"),
    "SubstanceNucleicAcidSubunitSugar": (None, ".substancenucleicacid"),
    "SubstancePolymer": (None, ".substancepolymer"),
    "SubstancePolymerMonomerSet": (None, ".substancepolymer"),
    "SubstancePolymerMonomerSetStartingMaterial": (None, ".substancepolymer"),
    "SubstancePolymerRepeat": (None, ".substancepolymer"),
    "SubstancePolymerRepeatRepeatUnit": (None, ".substancepolymer"),
    "SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation": (
        None,
        ".substancepolymer",
    ),
    "SubstancePolymerRepeatRepeatUnitStructuralRepresentation": (
        None,
        ".substancepolymer",
    ),
    "SubstanceProtein": (None, ".substanceprotein"),
    "SubstanceProteinSubunit": (None, ".substanceprotein"),
    "SubstanceReferenceInformation": (None, ".substancereferenceinformation"),
    "SubstanceReferenceInformationGene": (None, ".substancereferenceinformation"),
    "SubstanceReferenceInformationGeneElement": (
        None,
        ".substancereferenceinformation",
    ),
    "SubstanceReferenceInformationTarget": (None, ".substancereferenceinformation"),
    "SubstanceSourceMaterial": (None, ".substancesourcematerial"),
    "SubstanceSourceMaterialFractionDescription": (None, ".substancesourcematerial"),
    "SubstanceSourceMaterialOrganism": (None, ".substancesourcematerial"),
    "SubstanceSourceMaterialOrganismAuthor": (None, ".substancesourcematerial"),
    "SubstanceSourceMaterialOrganismHybrid": (None, ".substancesourcematerial"),
    "SubstanceSourceMaterialOrganismOrganismGeneral": (
        None,
        ".substancesourcematerial",
    ),
    "SubstanceSourceMaterialPartDescription": (None, ".substancesourcematerial"),
    "SupplyDelivery": (None, ".supplydelivery"),
    "SupplyDeliverySuppliedItem": (None, ".supplydelivery"),
    "SupplyRequest": (None, ".supplyrequest"),
    "SupplyRequestParameter": (None, ".supplyrequest"),
    "Task": (None, ".task"),
    "TaskInput": (None, ".task"),
    "TaskOutput": (None, ".task"),
    "TaskPerformer": (None, ".task"),
    "TaskRestriction": (None, ".task"),
    "TerminologyCapabilities": (None, ".terminologycapabilities"),
    "TerminologyCapabilitiesClosure": (None, ".terminologycapabilities"),
    "TerminologyCapabilitiesCodeSystem": (None, ".terminologycapabilities"),
    "TerminologyCapabilitiesCodeSystemVersion": (None, ".terminologycapabilities"),
    "TerminologyCapabilitiesCodeSystemVersionFilter": (
        None,
        ".terminologycapabilities",
    ),
    "TerminologyCapabilitiesExpansion": (None, ".terminologycapabilities"),
    "TerminologyCapabilitiesExpansionParameter": (None, ".terminologycapabilities"),
    "TerminologyCapabilitiesImplementation": (None, ".terminologycapabilities"),
    "TerminologyCapabilitiesSoftware": (None, ".terminologycapabilities"),
    "TerminologyCapabilitiesTranslation": (None, ".terminologycapabilities"),
    "TerminologyCapabilitiesValidateCode": (None, ".terminologycapabilities"),
    "TestPlan": (None, ".testplan"),
    "TestPlanDependency": (None, ".testplan"),
    "TestPlanTestCase": (None, ".testplan"),
    "TestPlanTestCaseAssertion": (None, ".testplan"),
    "TestPlanTestCaseDependency": (None, ".testplan"),
    "TestPlanTestCaseTestData": (None, ".testplan"),
    "TestPlanTestCaseTestRun": (None, ".testplan"),
    "TestPlanTestCaseTestRunScript": (None, ".testplan"),
    "TestReport": (None, ".testreport"),
    "TestReportParticipant": (None, ".testreport"),
    "TestReportSetup": (None, ".testreport"),
    "TestReportSetupAction": (None, ".testreport"),
    "TestReportSetupActionAssert": (None, ".testreport"),
    "TestReportSetupActionAssertRequirement": (None, ".testreport"),
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
    "TestScriptScope": (None, ".testscript"),
    "TestScriptSetup": (None, ".testscript"),
    "TestScriptSetupAction": (None, ".testscript"),
    "TestScriptSetupActionAssert": (None, ".testscript"),
    "TestScriptSetupActionAssertRequirement": (None, ".testscript"),
    "TestScriptSetupActionOperation": (None, ".testscript"),
    "TestScriptSetupActionOperationRequestHeader": (None, ".testscript"),
    "TestScriptTeardown": (None, ".testscript"),
    "TestScriptTeardownAction": (None, ".testscript"),
    "TestScriptTest": (None, ".testscript"),
    "TestScriptTestAction": (None, ".testscript"),
    "TestScriptVariable": (None, ".testscript"),
    "Timing": (None, ".timing"),
    "TimingRepeat": (None, ".timing"),
    "Transport": (None, ".transport"),
    "TransportInput": (None, ".transport"),
    "TransportOutput": (None, ".transport"),
    "TransportRestriction": (None, ".transport"),
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
    "ValueSetExpansionContainsProperty": (None, ".valueset"),
    "ValueSetExpansionContainsPropertySubProperty": (None, ".valueset"),
    "ValueSetExpansionParameter": (None, ".valueset"),
    "ValueSetExpansionProperty": (None, ".valueset"),
    "ValueSetScope": (None, ".valueset"),
    "VerificationResult": (None, ".verificationresult"),
    "VerificationResultAttestation": (None, ".verificationresult"),
    "VerificationResultPrimarySource": (None, ".verificationresult"),
    "VerificationResultValidator": (None, ".verificationresult"),
    "VirtualServiceDetail": (None, ".virtualservicedetail"),
    "VisionPrescription": (None, ".visionprescription"),
    "VisionPrescriptionLensSpecification": (None, ".visionprescription"),
    "VisionPrescriptionLensSpecificationPrism": (None, ".visionprescription"),
}


def get_fhir_model_class(model_name: str) -> typing.Type[FHIRAbstractModel]:
    """ """
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


def accountbalance_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AccountBalance", v)


def accountcoverage_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AccountCoverage", v)


def accountdiagnosis_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AccountDiagnosis", v)


def accountguarantor_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AccountGuarantor", v)


def accountprocedure_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AccountProcedure", v)


def accountrelatedaccount_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AccountRelatedAccount", v)


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


def actordefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ActorDefinition", v)


def address_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Address", v)


def administrableproductdefinition_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("AdministrableProductDefinition", v)


def administrableproductdefinitionproperty_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("AdministrableProductDefinitionProperty", v)


def administrableproductdefinitionrouteofadministration_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator(
        "AdministrableProductDefinitionRouteOfAdministration", v
    )


def administrableproductdefinitionrouteofadministrationtargetspecies_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator(
        "AdministrableProductDefinitionRouteOfAdministrationTargetSpecies", v
    )


def administrableproductdefinitionrouteofadministrationtargetspecieswithdrawalperiod_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator(
        "AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod",
        v,
    )


def adverseevent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AdverseEvent", v)


def adverseeventcontributingfactor_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("AdverseEventContributingFactor", v)


def adverseeventmitigatingaction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("AdverseEventMitigatingAction", v)


def adverseeventparticipant_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("AdverseEventParticipant", v)


def adverseeventpreventiveaction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("AdverseEventPreventiveAction", v)


def adverseeventsupportinginfo_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("AdverseEventSupportingInfo", v)


def adverseeventsuspectentity_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("AdverseEventSuspectEntity", v)


def adverseeventsuspectentitycausality_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("AdverseEventSuspectEntityCausality", v)


def age_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Age", v)


def allergyintolerance_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AllergyIntolerance", v)


def allergyintoleranceparticipant_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("AllergyIntoleranceParticipant", v)


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


def appointmentrecurrencetemplate_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("AppointmentRecurrenceTemplate", v)


def appointmentrecurrencetemplatemonthlytemplate_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("AppointmentRecurrenceTemplateMonthlyTemplate", v)


def appointmentrecurrencetemplateweeklytemplate_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("AppointmentRecurrenceTemplateWeeklyTemplate", v)


def appointmentrecurrencetemplateyearlytemplate_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("AppointmentRecurrenceTemplateYearlyTemplate", v)


def appointmentresponse_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AppointmentResponse", v)


def artifactassessment_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ArtifactAssessment", v)


def artifactassessmentcontent_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ArtifactAssessmentContent", v)


def attachment_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Attachment", v)


def auditevent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEvent", v)


def auditeventagent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEventAgent", v)


def auditevententity_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEventEntity", v)


def auditevententitydetail_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEventEntityDetail", v)


def auditeventoutcome_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEventOutcome", v)


def auditeventsource_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEventSource", v)


def availability_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Availability", v)


def availabilityavailabletime_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("AvailabilityAvailableTime", v)


def availabilitynotavailabletime_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("AvailabilityNotAvailableTime", v)


def backboneelement_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("BackboneElement", v)


def backbonetype_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("BackboneType", v)


def base_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Base", v)


def basic_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Basic", v)


def binary_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Binary", v)


def biologicallyderivedproduct_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("BiologicallyDerivedProduct", v)


def biologicallyderivedproductcollection_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("BiologicallyDerivedProductCollection", v)


def biologicallyderivedproductdispense_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("BiologicallyDerivedProductDispense", v)


def biologicallyderivedproductdispenseperformer_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("BiologicallyDerivedProductDispensePerformer", v)


def biologicallyderivedproductproperty_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("BiologicallyDerivedProductProperty", v)


def bodystructure_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("BodyStructure", v)


def bodystructureincludedstructure_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("BodyStructureIncludedStructure", v)


def bodystructureincludedstructurebodylandmarkorientation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator(
        "BodyStructureIncludedStructureBodyLandmarkOrientation", v
    )


def bodystructureincludedstructurebodylandmarkorientationdistancefromlandmark_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator(
        "BodyStructureIncludedStructureBodyLandmarkOrientationDistanceFromLandmark", v
    )


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


def canonicalresource_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CanonicalResource", v)


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


def capabilitystatementrestresource_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CapabilityStatementRestResource", v)


def capabilitystatementrestresourceinteraction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CapabilityStatementRestResourceInteraction", v)


def capabilitystatementrestresourceoperation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CapabilityStatementRestResourceOperation", v)


def capabilitystatementrestresourcesearchparam_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CapabilityStatementRestResourceSearchParam", v)


def capabilitystatementrestsecurity_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CapabilityStatementRestSecurity", v)


def capabilitystatementsoftware_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CapabilityStatementSoftware", v)


def careplan_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CarePlan", v)


def careplanactivity_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CarePlanActivity", v)


def careteam_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CareTeam", v)


def careteamparticipant_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CareTeamParticipant", v)


def chargeitem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ChargeItem", v)


def chargeitemdefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ChargeItemDefinition", v)


def chargeitemdefinitionapplicability_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ChargeItemDefinitionApplicability", v)


def chargeitemdefinitionpropertygroup_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ChargeItemDefinitionPropertyGroup", v)


def chargeitemperformer_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ChargeItemPerformer", v)


def citation_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Citation", v)


def citationcitedartifact_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CitationCitedArtifact", v)


def citationcitedartifactabstract_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CitationCitedArtifactAbstract", v)


def citationcitedartifactclassification_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CitationCitedArtifactClassification", v)


def citationcitedartifactcontributorship_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CitationCitedArtifactContributorship", v)


def citationcitedartifactcontributorshipentry_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CitationCitedArtifactContributorshipEntry", v)


def citationcitedartifactcontributorshipentrycontributioninstance_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator(
        "CitationCitedArtifactContributorshipEntryContributionInstance", v
    )


def citationcitedartifactcontributorshipsummary_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CitationCitedArtifactContributorshipSummary", v)


def citationcitedartifactpart_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CitationCitedArtifactPart", v)


def citationcitedartifactpublicationform_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CitationCitedArtifactPublicationForm", v)


def citationcitedartifactpublicationformpublishedin_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CitationCitedArtifactPublicationFormPublishedIn", v)


def citationcitedartifactrelatesto_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CitationCitedArtifactRelatesTo", v)


def citationcitedartifactstatusdate_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CitationCitedArtifactStatusDate", v)


def citationcitedartifacttitle_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CitationCitedArtifactTitle", v)


def citationcitedartifactversion_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CitationCitedArtifactVersion", v)


def citationcitedartifactweblocation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CitationCitedArtifactWebLocation", v)


def citationclassification_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CitationClassification", v)


def citationstatusdate_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CitationStatusDate", v)


def citationsummary_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CitationSummary", v)


def claim_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Claim", v)


def claimaccident_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimAccident", v)


def claimcareteam_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimCareTeam", v)


def claimdiagnosis_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimDiagnosis", v)


def claimevent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimEvent", v)


def claiminsurance_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimInsurance", v)


def claimitem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimItem", v)


def claimitembodysite_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimItemBodySite", v)


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


def claimresponseadditembodysite_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClaimResponseAddItemBodySite", v)


def claimresponseadditemdetail_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClaimResponseAddItemDetail", v)


def claimresponseadditemdetailsubdetail_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClaimResponseAddItemDetailSubDetail", v)


def claimresponseerror_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimResponseError", v)


def claimresponseevent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimResponseEvent", v)


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


def claimresponseitemreviewoutcome_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClaimResponseItemReviewOutcome", v)


def claimresponsepayment_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimResponsePayment", v)


def claimresponseprocessnote_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClaimResponseProcessNote", v)


def claimresponsetotal_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimResponseTotal", v)


def claimsupportinginfo_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClaimSupportingInfo", v)


def clinicalimpression_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClinicalImpression", v)


def clinicalimpressionfinding_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClinicalImpressionFinding", v)


def clinicalusedefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ClinicalUseDefinition", v)


def clinicalusedefinitioncontraindication_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClinicalUseDefinitionContraindication", v)


def clinicalusedefinitioncontraindicationothertherapy_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClinicalUseDefinitionContraindicationOtherTherapy", v)


def clinicalusedefinitionindication_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClinicalUseDefinitionIndication", v)


def clinicalusedefinitioninteraction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClinicalUseDefinitionInteraction", v)


def clinicalusedefinitioninteractioninteractant_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClinicalUseDefinitionInteractionInteractant", v)


def clinicalusedefinitionundesirableeffect_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClinicalUseDefinitionUndesirableEffect", v)


def clinicalusedefinitionwarning_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClinicalUseDefinitionWarning", v)


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


def codeablereference_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CodeableReference", v)


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


def compositionsection_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CompositionSection", v)


def conceptmap_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConceptMap", v)


def conceptmapadditionalattribute_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ConceptMapAdditionalAttribute", v)


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


def conceptmapgroupelementtargetproperty_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ConceptMapGroupElementTargetProperty", v)


def conceptmapgroupunmapped_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ConceptMapGroupUnmapped", v)


def conceptmapproperty_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConceptMapProperty", v)


def condition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Condition", v)


def conditiondefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConditionDefinition", v)


def conditiondefinitionmedication_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ConditionDefinitionMedication", v)


def conditiondefinitionobservation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ConditionDefinitionObservation", v)


def conditiondefinitionplan_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ConditionDefinitionPlan", v)


def conditiondefinitionprecondition_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ConditionDefinitionPrecondition", v)


def conditiondefinitionquestionnaire_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ConditionDefinitionQuestionnaire", v)


def conditionparticipant_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConditionParticipant", v)


def conditionstage_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConditionStage", v)


def consent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Consent", v)


def consentpolicybasis_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConsentPolicyBasis", v)


def consentprovision_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConsentProvision", v)


def consentprovisionactor_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConsentProvisionActor", v)


def consentprovisiondata_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConsentProvisionData", v)


def consentverification_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConsentVerification", v)


def contactdetail_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContactDetail", v)


def contactpoint_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContactPoint", v)


def contract_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Contract", v)


def contractcontentdefinition_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ContractContentDefinition", v)


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


def contracttermaction_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContractTermAction", v)


def contracttermactionsubject_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ContractTermActionSubject", v)


def contracttermasset_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContractTermAsset", v)


def contracttermassetcontext_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ContractTermAssetContext", v)


def contracttermassetvalueditem_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ContractTermAssetValuedItem", v)


def contracttermoffer_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContractTermOffer", v)


def contracttermofferanswer_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ContractTermOfferAnswer", v)


def contracttermofferparty_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContractTermOfferParty", v)


def contracttermsecuritylabel_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ContractTermSecurityLabel", v)


def contributor_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Contributor", v)


def count_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Count", v)


def coverage_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Coverage", v)


def coverageclass_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CoverageClass", v)


def coveragecosttobeneficiary_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CoverageCostToBeneficiary", v)


def coveragecosttobeneficiaryexception_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CoverageCostToBeneficiaryException", v)


def coverageeligibilityrequest_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CoverageEligibilityRequest", v)


def coverageeligibilityrequestevent_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CoverageEligibilityRequestEvent", v)


def coverageeligibilityrequestinsurance_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CoverageEligibilityRequestInsurance", v)


def coverageeligibilityrequestitem_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CoverageEligibilityRequestItem", v)


def coverageeligibilityrequestitemdiagnosis_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CoverageEligibilityRequestItemDiagnosis", v)


def coverageeligibilityrequestsupportinginfo_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CoverageEligibilityRequestSupportingInfo", v)


def coverageeligibilityresponse_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CoverageEligibilityResponse", v)


def coverageeligibilityresponseerror_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CoverageEligibilityResponseError", v)


def coverageeligibilityresponseevent_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CoverageEligibilityResponseEvent", v)


def coverageeligibilityresponseinsurance_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CoverageEligibilityResponseInsurance", v)


def coverageeligibilityresponseinsuranceitem_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CoverageEligibilityResponseInsuranceItem", v)


def coverageeligibilityresponseinsuranceitembenefit_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CoverageEligibilityResponseInsuranceItemBenefit", v)


def coveragepaymentby_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CoveragePaymentBy", v)


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


def datarequirementsort_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DataRequirementSort", v)


def datarequirementvaluefilter_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DataRequirementValueFilter", v)


def datatype_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DataType", v)


def detectedissue_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DetectedIssue", v)


def detectedissueevidence_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DetectedIssueEvidence", v)


def detectedissuemitigation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DetectedIssueMitigation", v)


def device_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Device", v)


def deviceassociation_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceAssociation", v)


def deviceassociationoperation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceAssociationOperation", v)


def deviceconformsto_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceConformsTo", v)


def devicedefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceDefinition", v)


def devicedefinitionchargeitem_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceDefinitionChargeItem", v)


def devicedefinitionclassification_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceDefinitionClassification", v)


def devicedefinitionconformsto_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceDefinitionConformsTo", v)


def devicedefinitioncorrectiveaction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceDefinitionCorrectiveAction", v)


def devicedefinitiondevicename_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceDefinitionDeviceName", v)


def devicedefinitionguideline_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceDefinitionGuideline", v)


def devicedefinitionhaspart_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceDefinitionHasPart", v)


def devicedefinitionlink_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceDefinitionLink", v)


def devicedefinitionmaterial_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceDefinitionMaterial", v)


def devicedefinitionpackaging_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceDefinitionPackaging", v)


def devicedefinitionpackagingdistributor_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceDefinitionPackagingDistributor", v)


def devicedefinitionproperty_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceDefinitionProperty", v)


def devicedefinitionregulatoryidentifier_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceDefinitionRegulatoryIdentifier", v)


def devicedefinitionudideviceidentifier_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceDefinitionUdiDeviceIdentifier", v)


def devicedefinitionudideviceidentifiermarketdistribution_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator(
        "DeviceDefinitionUdiDeviceIdentifierMarketDistribution", v
    )


def devicedefinitionversion_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceDefinitionVersion", v)


def devicedispense_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceDispense", v)


def devicedispenseperformer_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceDispensePerformer", v)


def devicemetric_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceMetric", v)


def devicemetriccalibration_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceMetricCalibration", v)


def devicename_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceName", v)


def deviceproperty_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceProperty", v)


def devicerequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceRequest", v)


def devicerequestparameter_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceRequestParameter", v)


def deviceudicarrier_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceUdiCarrier", v)


def deviceusage_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceUsage", v)


def deviceusageadherence_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceUsageAdherence", v)


def deviceversion_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceVersion", v)


def diagnosticreport_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DiagnosticReport", v)


def diagnosticreportmedia_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DiagnosticReportMedia", v)


def diagnosticreportsupportinginfo_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DiagnosticReportSupportingInfo", v)


def distance_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Distance", v)


def documentreference_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DocumentReference", v)


def documentreferenceattester_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DocumentReferenceAttester", v)


def documentreferencecontent_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DocumentReferenceContent", v)


def documentreferencecontentprofile_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DocumentReferenceContentProfile", v)


def documentreferencerelatesto_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DocumentReferenceRelatesTo", v)


def domainresource_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DomainResource", v)


def dosage_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Dosage", v)


def dosagedoseandrate_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DosageDoseAndRate", v)


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


def elementdefinitionbindingadditional_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ElementDefinitionBindingAdditional", v)


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


def encounter_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Encounter", v)


def encounteradmission_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EncounterAdmission", v)


def encounterdiagnosis_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EncounterDiagnosis", v)


def encounterhistory_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EncounterHistory", v)


def encounterhistorylocation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("EncounterHistoryLocation", v)


def encounterlocation_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EncounterLocation", v)


def encounterparticipant_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EncounterParticipant", v)


def encounterreason_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EncounterReason", v)


def endpoint_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Endpoint", v)


def endpointpayload_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EndpointPayload", v)


def enrollmentrequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EnrollmentRequest", v)


def enrollmentresponse_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EnrollmentResponse", v)


def episodeofcare_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EpisodeOfCare", v)


def episodeofcarediagnosis_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EpisodeOfCareDiagnosis", v)


def episodeofcarereason_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EpisodeOfCareReason", v)


def episodeofcarestatushistory_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("EpisodeOfCareStatusHistory", v)


def eventdefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EventDefinition", v)


def evidence_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Evidence", v)


def evidencecertainty_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EvidenceCertainty", v)


def evidencereport_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EvidenceReport", v)


def evidencereportrelatesto_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("EvidenceReportRelatesTo", v)


def evidencereportrelatestotarget_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("EvidenceReportRelatesToTarget", v)


def evidencereportsection_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EvidenceReportSection", v)


def evidencereportsubject_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EvidenceReportSubject", v)


def evidencereportsubjectcharacteristic_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("EvidenceReportSubjectCharacteristic", v)


def evidencestatistic_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EvidenceStatistic", v)


def evidencestatisticattributeestimate_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("EvidenceStatisticAttributeEstimate", v)


def evidencestatisticmodelcharacteristic_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("EvidenceStatisticModelCharacteristic", v)


def evidencestatisticmodelcharacteristicvariable_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("EvidenceStatisticModelCharacteristicVariable", v)


def evidencestatisticsamplesize_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("EvidenceStatisticSampleSize", v)


def evidencevariable_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("EvidenceVariable", v)


def evidencevariablecategory_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("EvidenceVariableCategory", v)


def evidencevariablecharacteristic_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("EvidenceVariableCharacteristic", v)


def evidencevariablecharacteristicdefinitionbycombination_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator(
        "EvidenceVariableCharacteristicDefinitionByCombination", v
    )


def evidencevariablecharacteristicdefinitionbytypeandvalue_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator(
        "EvidenceVariableCharacteristicDefinitionByTypeAndValue", v
    )


def evidencevariablecharacteristictimefromevent_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("EvidenceVariableCharacteristicTimeFromEvent", v)


def evidencevariabledefinition_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("EvidenceVariableDefinition", v)


def examplescenario_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ExampleScenario", v)


def examplescenarioactor_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ExampleScenarioActor", v)


def examplescenarioinstance_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExampleScenarioInstance", v)


def examplescenarioinstancecontainedinstance_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExampleScenarioInstanceContainedInstance", v)


def examplescenarioinstanceversion_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExampleScenarioInstanceVersion", v)


def examplescenarioprocess_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ExampleScenarioProcess", v)


def examplescenarioprocessstep_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExampleScenarioProcessStep", v)


def examplescenarioprocessstepalternative_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExampleScenarioProcessStepAlternative", v)


def examplescenarioprocessstepoperation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExampleScenarioProcessStepOperation", v)


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


def explanationofbenefitadditembodysite_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitAddItemBodySite", v)


def explanationofbenefitadditemdetail_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitAddItemDetail", v)


def explanationofbenefitadditemdetailsubdetail_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitAddItemDetailSubDetail", v)


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


def explanationofbenefitevent_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitEvent", v)


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


def explanationofbenefititembodysite_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitItemBodySite", v)


def explanationofbenefititemdetail_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitItemDetail", v)


def explanationofbenefititemdetailsubdetail_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitItemDetailSubDetail", v)


def explanationofbenefititemreviewoutcome_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitItemReviewOutcome", v)


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


def explanationofbenefitsupportinginfo_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitSupportingInfo", v)


def explanationofbenefittotal_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ExplanationOfBenefitTotal", v)


def expression_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Expression", v)


def extendedcontactdetail_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ExtendedContactDetail", v)


def extension_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Extension", v)


def familymemberhistory_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("FamilyMemberHistory", v)


def familymemberhistorycondition_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("FamilyMemberHistoryCondition", v)


def familymemberhistoryparticipant_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("FamilyMemberHistoryParticipant", v)


def familymemberhistoryprocedure_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("FamilyMemberHistoryProcedure", v)


def flag_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Flag", v)


def formularyitem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("FormularyItem", v)


def genomicstudy_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("GenomicStudy", v)


def genomicstudyanalysis_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("GenomicStudyAnalysis", v)


def genomicstudyanalysisdevice_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("GenomicStudyAnalysisDevice", v)


def genomicstudyanalysisinput_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("GenomicStudyAnalysisInput", v)


def genomicstudyanalysisoutput_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("GenomicStudyAnalysisOutput", v)


def genomicstudyanalysisperformer_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("GenomicStudyAnalysisPerformer", v)


def goal_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Goal", v)


def goaltarget_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("GoalTarget", v)


def graphdefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("GraphDefinition", v)


def graphdefinitionlink_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("GraphDefinitionLink", v)


def graphdefinitionlinkcompartment_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("GraphDefinitionLinkCompartment", v)


def graphdefinitionnode_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("GraphDefinitionNode", v)


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


def healthcareserviceeligibility_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("HealthcareServiceEligibility", v)


def humanname_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("HumanName", v)


def identifier_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Identifier", v)


def imagingselection_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ImagingSelection", v)


def imagingselectioninstance_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImagingSelectionInstance", v)


def imagingselectioninstanceimageregion2d_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImagingSelectionInstanceImageRegion2D", v)


def imagingselectioninstanceimageregion3d_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImagingSelectionInstanceImageRegion3D", v)


def imagingselectionperformer_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImagingSelectionPerformer", v)


def imagingstudy_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ImagingStudy", v)


def imagingstudyseries_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ImagingStudySeries", v)


def imagingstudyseriesinstance_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImagingStudySeriesInstance", v)


def imagingstudyseriesperformer_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImagingStudySeriesPerformer", v)


def immunization_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Immunization", v)


def immunizationevaluation_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ImmunizationEvaluation", v)


def immunizationperformer_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ImmunizationPerformer", v)


def immunizationprogrameligibility_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImmunizationProgramEligibility", v)


def immunizationprotocolapplied_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImmunizationProtocolApplied", v)


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


def implementationguide_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ImplementationGuide", v)


def implementationguidedefinition_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImplementationGuideDefinition", v)


def implementationguidedefinitiongrouping_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImplementationGuideDefinitionGrouping", v)


def implementationguidedefinitionpage_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImplementationGuideDefinitionPage", v)


def implementationguidedefinitionparameter_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImplementationGuideDefinitionParameter", v)


def implementationguidedefinitionresource_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImplementationGuideDefinitionResource", v)


def implementationguidedefinitiontemplate_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImplementationGuideDefinitionTemplate", v)


def implementationguidedependson_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImplementationGuideDependsOn", v)


def implementationguideglobal_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImplementationGuideGlobal", v)


def implementationguidemanifest_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImplementationGuideManifest", v)


def implementationguidemanifestpage_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImplementationGuideManifestPage", v)


def implementationguidemanifestresource_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ImplementationGuideManifestResource", v)


def ingredient_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Ingredient", v)


def ingredientmanufacturer_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("IngredientManufacturer", v)


def ingredientsubstance_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("IngredientSubstance", v)


def ingredientsubstancestrength_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("IngredientSubstanceStrength", v)


def ingredientsubstancestrengthreferencestrength_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("IngredientSubstanceStrengthReferenceStrength", v)


def insuranceplan_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("InsurancePlan", v)


def insuranceplancoverage_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("InsurancePlanCoverage", v)


def insuranceplancoveragebenefit_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("InsurancePlanCoverageBenefit", v)


def insuranceplancoveragebenefitlimit_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("InsurancePlanCoverageBenefitLimit", v)


def insuranceplanplan_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("InsurancePlanPlan", v)


def insuranceplanplangeneralcost_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("InsurancePlanPlanGeneralCost", v)


def insuranceplanplanspecificcost_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("InsurancePlanPlanSpecificCost", v)


def insuranceplanplanspecificcostbenefit_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("InsurancePlanPlanSpecificCostBenefit", v)


def insuranceplanplanspecificcostbenefitcost_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("InsurancePlanPlanSpecificCostBenefitCost", v)


def inventoryitem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("InventoryItem", v)


def inventoryitemassociation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("InventoryItemAssociation", v)


def inventoryitemcharacteristic_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("InventoryItemCharacteristic", v)


def inventoryitemdescription_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("InventoryItemDescription", v)


def inventoryiteminstance_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("InventoryItemInstance", v)


def inventoryitemname_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("InventoryItemName", v)


def inventoryitemresponsibleorganization_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("InventoryItemResponsibleOrganization", v)


def inventoryreport_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("InventoryReport", v)


def inventoryreportinventorylisting_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("InventoryReportInventoryListing", v)


def inventoryreportinventorylistingitem_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("InventoryReportInventoryListingItem", v)


def invoice_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Invoice", v)


def invoicelineitem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("InvoiceLineItem", v)


def invoiceparticipant_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("InvoiceParticipant", v)


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


def manufactureditemdefinition_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ManufacturedItemDefinition", v)


def manufactureditemdefinitioncomponent_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ManufacturedItemDefinitionComponent", v)


def manufactureditemdefinitioncomponentconstituent_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ManufacturedItemDefinitionComponentConstituent", v)


def manufactureditemdefinitionproperty_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ManufacturedItemDefinitionProperty", v)


def marketingstatus_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MarketingStatus", v)


def measure_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Measure", v)


def measuregroup_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MeasureGroup", v)


def measuregrouppopulation_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MeasureGroupPopulation", v)


def measuregroupstratifier_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MeasureGroupStratifier", v)


def measuregroupstratifiercomponent_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MeasureGroupStratifierComponent", v)


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


def measurereportgroupstratifierstratumcomponent_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MeasureReportGroupStratifierStratumComponent", v)


def measurereportgroupstratifierstratumpopulation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MeasureReportGroupStratifierStratumPopulation", v)


def measuresupplementaldata_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MeasureSupplementalData", v)


def measureterm_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MeasureTerm", v)


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


def medicationbatch_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MedicationBatch", v)


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


def medicationknowledge_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MedicationKnowledge", v)


def medicationknowledgecost_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationKnowledgeCost", v)


def medicationknowledgedefinitional_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationKnowledgeDefinitional", v)


def medicationknowledgedefinitionaldrugcharacteristic_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationKnowledgeDefinitionalDrugCharacteristic", v)


def medicationknowledgedefinitionalingredient_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationKnowledgeDefinitionalIngredient", v)


def medicationknowledgeindicationguideline_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationKnowledgeIndicationGuideline", v)


def medicationknowledgeindicationguidelinedosingguideline_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator(
        "MedicationKnowledgeIndicationGuidelineDosingGuideline", v
    )


def medicationknowledgeindicationguidelinedosingguidelinedosage_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator(
        "MedicationKnowledgeIndicationGuidelineDosingGuidelineDosage", v
    )


def medicationknowledgeindicationguidelinedosingguidelinepatientcharacteristic_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator(
        "MedicationKnowledgeIndicationGuidelineDosingGuidelinePatientCharacteristic", v
    )


def medicationknowledgemedicineclassification_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationKnowledgeMedicineClassification", v)


def medicationknowledgemonitoringprogram_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationKnowledgeMonitoringProgram", v)


def medicationknowledgemonograph_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationKnowledgeMonograph", v)


def medicationknowledgepackaging_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationKnowledgePackaging", v)


def medicationknowledgeregulatory_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationKnowledgeRegulatory", v)


def medicationknowledgeregulatorymaxdispense_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationKnowledgeRegulatoryMaxDispense", v)


def medicationknowledgeregulatorysubstitution_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationKnowledgeRegulatorySubstitution", v)


def medicationknowledgerelatedmedicationknowledge_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationKnowledgeRelatedMedicationKnowledge", v)


def medicationknowledgestorageguideline_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationKnowledgeStorageGuideline", v)


def medicationknowledgestorageguidelineenvironmentalsetting_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator(
        "MedicationKnowledgeStorageGuidelineEnvironmentalSetting", v
    )


def medicationrequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MedicationRequest", v)


def medicationrequestdispenserequest_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationRequestDispenseRequest", v)


def medicationrequestdispenserequestinitialfill_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationRequestDispenseRequestInitialFill", v)


def medicationrequestsubstitution_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationRequestSubstitution", v)


def medicationstatement_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MedicationStatement", v)


def medicationstatementadherence_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationStatementAdherence", v)


def medicinalproductdefinition_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicinalProductDefinition", v)


def medicinalproductdefinitioncharacteristic_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicinalProductDefinitionCharacteristic", v)


def medicinalproductdefinitioncontact_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicinalProductDefinitionContact", v)


def medicinalproductdefinitioncrossreference_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicinalProductDefinitionCrossReference", v)


def medicinalproductdefinitionname_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicinalProductDefinitionName", v)


def medicinalproductdefinitionnamepart_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicinalProductDefinitionNamePart", v)


def medicinalproductdefinitionnameusage_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicinalProductDefinitionNameUsage", v)


def medicinalproductdefinitionoperation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicinalProductDefinitionOperation", v)


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


def molecularsequence_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MolecularSequence", v)


def molecularsequencerelative_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MolecularSequenceRelative", v)


def molecularsequencerelativeedit_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MolecularSequenceRelativeEdit", v)


def molecularsequencerelativestartingsequence_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MolecularSequenceRelativeStartingSequence", v)


def monetarycomponent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MonetaryComponent", v)


def money_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Money", v)


def namingsystem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("NamingSystem", v)


def namingsystemuniqueid_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("NamingSystemUniqueId", v)


def narrative_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Narrative", v)


def nutritionintake_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("NutritionIntake", v)


def nutritionintakeconsumeditem_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionIntakeConsumedItem", v)


def nutritionintakeingredientlabel_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionIntakeIngredientLabel", v)


def nutritionintakeperformer_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionIntakePerformer", v)


def nutritionorder_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("NutritionOrder", v)


def nutritionorderenteralformula_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionOrderEnteralFormula", v)


def nutritionorderenteralformulaadditive_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionOrderEnteralFormulaAdditive", v)


def nutritionorderenteralformulaadministration_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionOrderEnteralFormulaAdministration", v)


def nutritionorderenteralformulaadministrationschedule_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionOrderEnteralFormulaAdministrationSchedule", v)


def nutritionorderoraldiet_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("NutritionOrderOralDiet", v)


def nutritionorderoraldietnutrient_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionOrderOralDietNutrient", v)


def nutritionorderoraldietschedule_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionOrderOralDietSchedule", v)


def nutritionorderoraldiettexture_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionOrderOralDietTexture", v)


def nutritionordersupplement_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionOrderSupplement", v)


def nutritionordersupplementschedule_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionOrderSupplementSchedule", v)


def nutritionproduct_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("NutritionProduct", v)


def nutritionproductcharacteristic_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionProductCharacteristic", v)


def nutritionproductingredient_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionProductIngredient", v)


def nutritionproductinstance_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionProductInstance", v)


def nutritionproductnutrient_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionProductNutrient", v)


def observation_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Observation", v)


def observationcomponent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ObservationComponent", v)


def observationdefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ObservationDefinition", v)


def observationdefinitioncomponent_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ObservationDefinitionComponent", v)


def observationdefinitionqualifiedvalue_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ObservationDefinitionQualifiedValue", v)


def observationreferencerange_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ObservationReferenceRange", v)


def observationtriggeredby_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ObservationTriggeredBy", v)


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


def operationdefinitionparameterreferencedfrom_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("OperationDefinitionParameterReferencedFrom", v)


def operationoutcome_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("OperationOutcome", v)


def operationoutcomeissue_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("OperationOutcomeIssue", v)


def organization_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Organization", v)


def organizationaffiliation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("OrganizationAffiliation", v)


def organizationqualification_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("OrganizationQualification", v)


def packagedproductdefinition_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PackagedProductDefinition", v)


def packagedproductdefinitionlegalstatusofsupply_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PackagedProductDefinitionLegalStatusOfSupply", v)


def packagedproductdefinitionpackaging_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PackagedProductDefinitionPackaging", v)


def packagedproductdefinitionpackagingcontaineditem_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PackagedProductDefinitionPackagingContainedItem", v)


def packagedproductdefinitionpackagingproperty_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PackagedProductDefinitionPackagingProperty", v)


def parameterdefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ParameterDefinition", v)


def parameters_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Parameters", v)


def parametersparameter_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ParametersParameter", v)


def patient_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Patient", v)


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


def paymentreconciliationallocation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PaymentReconciliationAllocation", v)


def paymentreconciliationprocessnote_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PaymentReconciliationProcessNote", v)


def period_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Period", v)


def permission_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Permission", v)


def permissionjustification_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PermissionJustification", v)


def permissionrule_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("PermissionRule", v)


def permissionruleactivity_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("PermissionRuleActivity", v)


def permissionruledata_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("PermissionRuleData", v)


def permissionruledataresource_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PermissionRuleDataResource", v)


def person_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Person", v)


def personcommunication_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("PersonCommunication", v)


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


def plandefinitionactioninput_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PlanDefinitionActionInput", v)


def plandefinitionactionoutput_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PlanDefinitionActionOutput", v)


def plandefinitionactionparticipant_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PlanDefinitionActionParticipant", v)


def plandefinitionactionrelatedaction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PlanDefinitionActionRelatedAction", v)


def plandefinitionactor_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("PlanDefinitionActor", v)


def plandefinitionactoroption_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PlanDefinitionActorOption", v)


def plandefinitiongoal_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("PlanDefinitionGoal", v)


def plandefinitiongoaltarget_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PlanDefinitionGoalTarget", v)


def practitioner_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Practitioner", v)


def practitionercommunication_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PractitionerCommunication", v)


def practitionerqualification_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PractitionerQualification", v)


def practitionerrole_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("PractitionerRole", v)


def primitivetype_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("PrimitiveType", v)


def procedure_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Procedure", v)


def procedurefocaldevice_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ProcedureFocalDevice", v)


def procedureperformer_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ProcedurePerformer", v)


def productshelflife_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ProductShelfLife", v)


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


def questionnaireitemansweroption_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("QuestionnaireItemAnswerOption", v)


def questionnaireitemenablewhen_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("QuestionnaireItemEnableWhen", v)


def questionnaireiteminitial_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("QuestionnaireItemInitial", v)


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


def ratiorange_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("RatioRange", v)


def reference_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Reference", v)


def regulatedauthorization_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("RegulatedAuthorization", v)


def regulatedauthorizationcase_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("RegulatedAuthorizationCase", v)


def relatedartifact_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("RelatedArtifact", v)


def relatedperson_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("RelatedPerson", v)


def relatedpersoncommunication_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("RelatedPersonCommunication", v)


def requestorchestration_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("RequestOrchestration", v)


def requestorchestrationaction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("RequestOrchestrationAction", v)


def requestorchestrationactioncondition_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("RequestOrchestrationActionCondition", v)


def requestorchestrationactiondynamicvalue_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("RequestOrchestrationActionDynamicValue", v)


def requestorchestrationactioninput_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("RequestOrchestrationActionInput", v)


def requestorchestrationactionoutput_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("RequestOrchestrationActionOutput", v)


def requestorchestrationactionparticipant_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("RequestOrchestrationActionParticipant", v)


def requestorchestrationactionrelatedaction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("RequestOrchestrationActionRelatedAction", v)


def requirements_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Requirements", v)


def requirementsstatement_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("RequirementsStatement", v)


def researchstudy_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ResearchStudy", v)


def researchstudyassociatedparty_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ResearchStudyAssociatedParty", v)


def researchstudycomparisongroup_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ResearchStudyComparisonGroup", v)


def researchstudylabel_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ResearchStudyLabel", v)


def researchstudyobjective_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ResearchStudyObjective", v)


def researchstudyoutcomemeasure_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ResearchStudyOutcomeMeasure", v)


def researchstudyprogressstatus_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ResearchStudyProgressStatus", v)


def researchstudyrecruitment_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ResearchStudyRecruitment", v)


def researchsubject_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ResearchSubject", v)


def researchsubjectprogress_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ResearchSubjectProgress", v)


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


def servicerequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ServiceRequest", v)


def servicerequestorderdetail_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ServiceRequestOrderDetail", v)


def servicerequestorderdetailparameter_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ServiceRequestOrderDetailParameter", v)


def servicerequestpatientinstruction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ServiceRequestPatientInstruction", v)


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


def specimendefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SpecimenDefinition", v)


def specimendefinitiontypetested_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SpecimenDefinitionTypeTested", v)


def specimendefinitiontypetestedcontainer_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SpecimenDefinitionTypeTestedContainer", v)


def specimendefinitiontypetestedcontaineradditive_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SpecimenDefinitionTypeTestedContainerAdditive", v)


def specimendefinitiontypetestedhandling_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SpecimenDefinitionTypeTestedHandling", v)


def specimenfeature_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SpecimenFeature", v)


def specimenprocessing_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SpecimenProcessing", v)


def structuredefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("StructureDefinition", v)


def structuredefinitioncontext_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("StructureDefinitionContext", v)


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


def structuremapconst_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("StructureMapConst", v)


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


def subscriptionfilterby_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SubscriptionFilterBy", v)


def subscriptionparameter_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SubscriptionParameter", v)


def subscriptionstatus_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SubscriptionStatus", v)


def subscriptionstatusnotificationevent_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubscriptionStatusNotificationEvent", v)


def subscriptiontopic_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SubscriptionTopic", v)


def subscriptiontopiccanfilterby_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubscriptionTopicCanFilterBy", v)


def subscriptiontopiceventtrigger_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubscriptionTopicEventTrigger", v)


def subscriptiontopicnotificationshape_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubscriptionTopicNotificationShape", v)


def subscriptiontopicresourcetrigger_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubscriptionTopicResourceTrigger", v)


def subscriptiontopicresourcetriggerquerycriteria_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubscriptionTopicResourceTriggerQueryCriteria", v)


def substance_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Substance", v)


def substancedefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SubstanceDefinition", v)


def substancedefinitioncharacterization_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceDefinitionCharacterization", v)


def substancedefinitioncode_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceDefinitionCode", v)


def substancedefinitionmoiety_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceDefinitionMoiety", v)


def substancedefinitionmolecularweight_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceDefinitionMolecularWeight", v)


def substancedefinitionname_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceDefinitionName", v)


def substancedefinitionnameofficial_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceDefinitionNameOfficial", v)


def substancedefinitionproperty_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceDefinitionProperty", v)


def substancedefinitionrelationship_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceDefinitionRelationship", v)


def substancedefinitionsourcematerial_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceDefinitionSourceMaterial", v)


def substancedefinitionstructure_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceDefinitionStructure", v)


def substancedefinitionstructurerepresentation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceDefinitionStructureRepresentation", v)


def substanceingredient_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SubstanceIngredient", v)


def substancenucleicacid_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SubstanceNucleicAcid", v)


def substancenucleicacidsubunit_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceNucleicAcidSubunit", v)


def substancenucleicacidsubunitlinkage_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceNucleicAcidSubunitLinkage", v)


def substancenucleicacidsubunitsugar_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceNucleicAcidSubunitSugar", v)


def substancepolymer_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SubstancePolymer", v)


def substancepolymermonomerset_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstancePolymerMonomerSet", v)


def substancepolymermonomersetstartingmaterial_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstancePolymerMonomerSetStartingMaterial", v)


def substancepolymerrepeat_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SubstancePolymerRepeat", v)


def substancepolymerrepeatrepeatunit_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstancePolymerRepeatRepeatUnit", v)


def substancepolymerrepeatrepeatunitdegreeofpolymerisation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator(
        "SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation", v
    )


def substancepolymerrepeatrepeatunitstructuralrepresentation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator(
        "SubstancePolymerRepeatRepeatUnitStructuralRepresentation", v
    )


def substanceprotein_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SubstanceProtein", v)


def substanceproteinsubunit_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceProteinSubunit", v)


def substancereferenceinformation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceReferenceInformation", v)


def substancereferenceinformationgene_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceReferenceInformationGene", v)


def substancereferenceinformationgeneelement_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceReferenceInformationGeneElement", v)


def substancereferenceinformationtarget_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceReferenceInformationTarget", v)


def substancesourcematerial_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceSourceMaterial", v)


def substancesourcematerialfractiondescription_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceSourceMaterialFractionDescription", v)


def substancesourcematerialorganism_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceSourceMaterialOrganism", v)


def substancesourcematerialorganismauthor_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceSourceMaterialOrganismAuthor", v)


def substancesourcematerialorganismhybrid_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceSourceMaterialOrganismHybrid", v)


def substancesourcematerialorganismorganismgeneral_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceSourceMaterialOrganismOrganismGeneral", v)


def substancesourcematerialpartdescription_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SubstanceSourceMaterialPartDescription", v)


def supplydelivery_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SupplyDelivery", v)


def supplydeliverysupplieditem_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("SupplyDeliverySuppliedItem", v)


def supplyrequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SupplyRequest", v)


def supplyrequestparameter_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SupplyRequestParameter", v)


def task_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Task", v)


def taskinput_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TaskInput", v)


def taskoutput_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TaskOutput", v)


def taskperformer_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TaskPerformer", v)


def taskrestriction_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TaskRestriction", v)


def terminologycapabilities_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TerminologyCapabilities", v)


def terminologycapabilitiesclosure_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TerminologyCapabilitiesClosure", v)


def terminologycapabilitiescodesystem_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TerminologyCapabilitiesCodeSystem", v)


def terminologycapabilitiescodesystemversion_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TerminologyCapabilitiesCodeSystemVersion", v)


def terminologycapabilitiescodesystemversionfilter_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TerminologyCapabilitiesCodeSystemVersionFilter", v)


def terminologycapabilitiesexpansion_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TerminologyCapabilitiesExpansion", v)


def terminologycapabilitiesexpansionparameter_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TerminologyCapabilitiesExpansionParameter", v)


def terminologycapabilitiesimplementation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TerminologyCapabilitiesImplementation", v)


def terminologycapabilitiessoftware_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TerminologyCapabilitiesSoftware", v)


def terminologycapabilitiestranslation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TerminologyCapabilitiesTranslation", v)


def terminologycapabilitiesvalidatecode_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TerminologyCapabilitiesValidateCode", v)


def testplan_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestPlan", v)


def testplandependency_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestPlanDependency", v)


def testplantestcase_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestPlanTestCase", v)


def testplantestcaseassertion_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestPlanTestCaseAssertion", v)


def testplantestcasedependency_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestPlanTestCaseDependency", v)


def testplantestcasetestdata_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestPlanTestCaseTestData", v)


def testplantestcasetestrun_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestPlanTestCaseTestRun", v)


def testplantestcasetestrunscript_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestPlanTestCaseTestRunScript", v)


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


def testreportsetupactionassertrequirement_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestReportSetupActionAssertRequirement", v)


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


def testscriptscope_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptScope", v)


def testscriptsetup_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptSetup", v)


def testscriptsetupaction_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptSetupAction", v)


def testscriptsetupactionassert_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestScriptSetupActionAssert", v)


def testscriptsetupactionassertrequirement_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestScriptSetupActionAssertRequirement", v)


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


def transport_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Transport", v)


def transportinput_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TransportInput", v)


def transportoutput_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TransportOutput", v)


def transportrestriction_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TransportRestriction", v)


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


def valuesetexpansioncontainsproperty_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ValueSetExpansionContainsProperty", v)


def valuesetexpansioncontainspropertysubproperty_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ValueSetExpansionContainsPropertySubProperty", v)


def valuesetexpansionparameter_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ValueSetExpansionParameter", v)


def valuesetexpansionproperty_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ValueSetExpansionProperty", v)


def valuesetscope_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ValueSetScope", v)


def verificationresult_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("VerificationResult", v)


def verificationresultattestation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("VerificationResultAttestation", v)


def verificationresultprimarysource_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("VerificationResultPrimarySource", v)


def verificationresultvalidator_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("VerificationResultValidator", v)


def virtualservicedetail_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("VirtualServiceDetail", v)


def visionprescription_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("VisionPrescription", v)


def visionprescriptionlensspecification_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("VisionPrescriptionLensSpecification", v)


def visionprescriptionlensspecificationprism_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("VisionPrescriptionLensSpecificationPrism", v)


__all__ = [
    "fhirprimitiveextension_validator",
    "account_validator",
    "accountbalance_validator",
    "accountcoverage_validator",
    "accountdiagnosis_validator",
    "accountguarantor_validator",
    "accountprocedure_validator",
    "accountrelatedaccount_validator",
    "activitydefinition_validator",
    "activitydefinitiondynamicvalue_validator",
    "activitydefinitionparticipant_validator",
    "actordefinition_validator",
    "address_validator",
    "administrableproductdefinition_validator",
    "administrableproductdefinitionproperty_validator",
    "administrableproductdefinitionrouteofadministration_validator",
    "administrableproductdefinitionrouteofadministrationtargetspecies_validator",
    "administrableproductdefinitionrouteofadministrationtargetspecieswithdrawalperiod_validator",  # noqa: B950
    "adverseevent_validator",
    "adverseeventcontributingfactor_validator",
    "adverseeventmitigatingaction_validator",
    "adverseeventparticipant_validator",
    "adverseeventpreventiveaction_validator",
    "adverseeventsupportinginfo_validator",
    "adverseeventsuspectentity_validator",
    "adverseeventsuspectentitycausality_validator",
    "age_validator",
    "allergyintolerance_validator",
    "allergyintoleranceparticipant_validator",
    "allergyintolerancereaction_validator",
    "annotation_validator",
    "appointment_validator",
    "appointmentparticipant_validator",
    "appointmentrecurrencetemplate_validator",
    "appointmentrecurrencetemplatemonthlytemplate_validator",
    "appointmentrecurrencetemplateweeklytemplate_validator",
    "appointmentrecurrencetemplateyearlytemplate_validator",
    "appointmentresponse_validator",
    "artifactassessment_validator",
    "artifactassessmentcontent_validator",
    "attachment_validator",
    "auditevent_validator",
    "auditeventagent_validator",
    "auditevententity_validator",
    "auditevententitydetail_validator",
    "auditeventoutcome_validator",
    "auditeventsource_validator",
    "availability_validator",
    "availabilityavailabletime_validator",
    "availabilitynotavailabletime_validator",
    "backboneelement_validator",
    "backbonetype_validator",
    "base_validator",
    "basic_validator",
    "binary_validator",
    "biologicallyderivedproduct_validator",
    "biologicallyderivedproductcollection_validator",
    "biologicallyderivedproductdispense_validator",
    "biologicallyderivedproductdispenseperformer_validator",
    "biologicallyderivedproductproperty_validator",
    "bodystructure_validator",
    "bodystructureincludedstructure_validator",
    "bodystructureincludedstructurebodylandmarkorientation_validator",
    "bodystructureincludedstructurebodylandmarkorientationdistancefromlandmark_validator",
    "bundle_validator",
    "bundleentry_validator",
    "bundleentryrequest_validator",
    "bundleentryresponse_validator",
    "bundleentrysearch_validator",
    "bundlelink_validator",
    "canonicalresource_validator",
    "capabilitystatement_validator",
    "capabilitystatementdocument_validator",
    "capabilitystatementimplementation_validator",
    "capabilitystatementmessaging_validator",
    "capabilitystatementmessagingendpoint_validator",
    "capabilitystatementmessagingsupportedmessage_validator",
    "capabilitystatementrest_validator",
    "capabilitystatementrestinteraction_validator",
    "capabilitystatementrestresource_validator",
    "capabilitystatementrestresourceinteraction_validator",
    "capabilitystatementrestresourceoperation_validator",
    "capabilitystatementrestresourcesearchparam_validator",
    "capabilitystatementrestsecurity_validator",
    "capabilitystatementsoftware_validator",
    "careplan_validator",
    "careplanactivity_validator",
    "careteam_validator",
    "careteamparticipant_validator",
    "chargeitem_validator",
    "chargeitemdefinition_validator",
    "chargeitemdefinitionapplicability_validator",
    "chargeitemdefinitionpropertygroup_validator",
    "chargeitemperformer_validator",
    "citation_validator",
    "citationcitedartifact_validator",
    "citationcitedartifactabstract_validator",
    "citationcitedartifactclassification_validator",
    "citationcitedartifactcontributorship_validator",
    "citationcitedartifactcontributorshipentry_validator",
    "citationcitedartifactcontributorshipentrycontributioninstance_validator",
    "citationcitedartifactcontributorshipsummary_validator",
    "citationcitedartifactpart_validator",
    "citationcitedartifactpublicationform_validator",
    "citationcitedartifactpublicationformpublishedin_validator",
    "citationcitedartifactrelatesto_validator",
    "citationcitedartifactstatusdate_validator",
    "citationcitedartifacttitle_validator",
    "citationcitedartifactversion_validator",
    "citationcitedartifactweblocation_validator",
    "citationclassification_validator",
    "citationstatusdate_validator",
    "citationsummary_validator",
    "claim_validator",
    "claimaccident_validator",
    "claimcareteam_validator",
    "claimdiagnosis_validator",
    "claimevent_validator",
    "claiminsurance_validator",
    "claimitem_validator",
    "claimitembodysite_validator",
    "claimitemdetail_validator",
    "claimitemdetailsubdetail_validator",
    "claimpayee_validator",
    "claimprocedure_validator",
    "claimrelated_validator",
    "claimresponse_validator",
    "claimresponseadditem_validator",
    "claimresponseadditembodysite_validator",
    "claimresponseadditemdetail_validator",
    "claimresponseadditemdetailsubdetail_validator",
    "claimresponseerror_validator",
    "claimresponseevent_validator",
    "claimresponseinsurance_validator",
    "claimresponseitem_validator",
    "claimresponseitemadjudication_validator",
    "claimresponseitemdetail_validator",
    "claimresponseitemdetailsubdetail_validator",
    "claimresponseitemreviewoutcome_validator",
    "claimresponsepayment_validator",
    "claimresponseprocessnote_validator",
    "claimresponsetotal_validator",
    "claimsupportinginfo_validator",
    "clinicalimpression_validator",
    "clinicalimpressionfinding_validator",
    "clinicalusedefinition_validator",
    "clinicalusedefinitioncontraindication_validator",
    "clinicalusedefinitioncontraindicationothertherapy_validator",
    "clinicalusedefinitionindication_validator",
    "clinicalusedefinitioninteraction_validator",
    "clinicalusedefinitioninteractioninteractant_validator",
    "clinicalusedefinitionundesirableeffect_validator",
    "clinicalusedefinitionwarning_validator",
    "codesystem_validator",
    "codesystemconcept_validator",
    "codesystemconceptdesignation_validator",
    "codesystemconceptproperty_validator",
    "codesystemfilter_validator",
    "codesystemproperty_validator",
    "codeableconcept_validator",
    "codeablereference_validator",
    "coding_validator",
    "communication_validator",
    "communicationpayload_validator",
    "communicationrequest_validator",
    "communicationrequestpayload_validator",
    "compartmentdefinition_validator",
    "compartmentdefinitionresource_validator",
    "composition_validator",
    "compositionattester_validator",
    "compositionevent_validator",
    "compositionsection_validator",
    "conceptmap_validator",
    "conceptmapadditionalattribute_validator",
    "conceptmapgroup_validator",
    "conceptmapgroupelement_validator",
    "conceptmapgroupelementtarget_validator",
    "conceptmapgroupelementtargetdependson_validator",
    "conceptmapgroupelementtargetproperty_validator",
    "conceptmapgroupunmapped_validator",
    "conceptmapproperty_validator",
    "condition_validator",
    "conditiondefinition_validator",
    "conditiondefinitionmedication_validator",
    "conditiondefinitionobservation_validator",
    "conditiondefinitionplan_validator",
    "conditiondefinitionprecondition_validator",
    "conditiondefinitionquestionnaire_validator",
    "conditionparticipant_validator",
    "conditionstage_validator",
    "consent_validator",
    "consentpolicybasis_validator",
    "consentprovision_validator",
    "consentprovisionactor_validator",
    "consentprovisiondata_validator",
    "consentverification_validator",
    "contactdetail_validator",
    "contactpoint_validator",
    "contract_validator",
    "contractcontentdefinition_validator",
    "contractfriendly_validator",
    "contractlegal_validator",
    "contractrule_validator",
    "contractsigner_validator",
    "contractterm_validator",
    "contracttermaction_validator",
    "contracttermactionsubject_validator",
    "contracttermasset_validator",
    "contracttermassetcontext_validator",
    "contracttermassetvalueditem_validator",
    "contracttermoffer_validator",
    "contracttermofferanswer_validator",
    "contracttermofferparty_validator",
    "contracttermsecuritylabel_validator",
    "contributor_validator",
    "count_validator",
    "coverage_validator",
    "coverageclass_validator",
    "coveragecosttobeneficiary_validator",
    "coveragecosttobeneficiaryexception_validator",
    "coverageeligibilityrequest_validator",
    "coverageeligibilityrequestevent_validator",
    "coverageeligibilityrequestinsurance_validator",
    "coverageeligibilityrequestitem_validator",
    "coverageeligibilityrequestitemdiagnosis_validator",
    "coverageeligibilityrequestsupportinginfo_validator",
    "coverageeligibilityresponse_validator",
    "coverageeligibilityresponseerror_validator",
    "coverageeligibilityresponseevent_validator",
    "coverageeligibilityresponseinsurance_validator",
    "coverageeligibilityresponseinsuranceitem_validator",
    "coverageeligibilityresponseinsuranceitembenefit_validator",
    "coveragepaymentby_validator",
    "datarequirement_validator",
    "datarequirementcodefilter_validator",
    "datarequirementdatefilter_validator",
    "datarequirementsort_validator",
    "datarequirementvaluefilter_validator",
    "datatype_validator",
    "detectedissue_validator",
    "detectedissueevidence_validator",
    "detectedissuemitigation_validator",
    "device_validator",
    "deviceassociation_validator",
    "deviceassociationoperation_validator",
    "deviceconformsto_validator",
    "devicedefinition_validator",
    "devicedefinitionchargeitem_validator",
    "devicedefinitionclassification_validator",
    "devicedefinitionconformsto_validator",
    "devicedefinitioncorrectiveaction_validator",
    "devicedefinitiondevicename_validator",
    "devicedefinitionguideline_validator",
    "devicedefinitionhaspart_validator",
    "devicedefinitionlink_validator",
    "devicedefinitionmaterial_validator",
    "devicedefinitionpackaging_validator",
    "devicedefinitionpackagingdistributor_validator",
    "devicedefinitionproperty_validator",
    "devicedefinitionregulatoryidentifier_validator",
    "devicedefinitionudideviceidentifier_validator",
    "devicedefinitionudideviceidentifiermarketdistribution_validator",
    "devicedefinitionversion_validator",
    "devicedispense_validator",
    "devicedispenseperformer_validator",
    "devicemetric_validator",
    "devicemetriccalibration_validator",
    "devicename_validator",
    "deviceproperty_validator",
    "devicerequest_validator",
    "devicerequestparameter_validator",
    "deviceudicarrier_validator",
    "deviceusage_validator",
    "deviceusageadherence_validator",
    "deviceversion_validator",
    "diagnosticreport_validator",
    "diagnosticreportmedia_validator",
    "diagnosticreportsupportinginfo_validator",
    "distance_validator",
    "documentreference_validator",
    "documentreferenceattester_validator",
    "documentreferencecontent_validator",
    "documentreferencecontentprofile_validator",
    "documentreferencerelatesto_validator",
    "domainresource_validator",
    "dosage_validator",
    "dosagedoseandrate_validator",
    "duration_validator",
    "element_validator",
    "elementdefinition_validator",
    "elementdefinitionbase_validator",
    "elementdefinitionbinding_validator",
    "elementdefinitionbindingadditional_validator",
    "elementdefinitionconstraint_validator",
    "elementdefinitionexample_validator",
    "elementdefinitionmapping_validator",
    "elementdefinitionslicing_validator",
    "elementdefinitionslicingdiscriminator_validator",
    "elementdefinitiontype_validator",
    "encounter_validator",
    "encounteradmission_validator",
    "encounterdiagnosis_validator",
    "encounterhistory_validator",
    "encounterhistorylocation_validator",
    "encounterlocation_validator",
    "encounterparticipant_validator",
    "encounterreason_validator",
    "endpoint_validator",
    "endpointpayload_validator",
    "enrollmentrequest_validator",
    "enrollmentresponse_validator",
    "episodeofcare_validator",
    "episodeofcarediagnosis_validator",
    "episodeofcarereason_validator",
    "episodeofcarestatushistory_validator",
    "eventdefinition_validator",
    "evidence_validator",
    "evidencecertainty_validator",
    "evidencereport_validator",
    "evidencereportrelatesto_validator",
    "evidencereportrelatestotarget_validator",
    "evidencereportsection_validator",
    "evidencereportsubject_validator",
    "evidencereportsubjectcharacteristic_validator",
    "evidencestatistic_validator",
    "evidencestatisticattributeestimate_validator",
    "evidencestatisticmodelcharacteristic_validator",
    "evidencestatisticmodelcharacteristicvariable_validator",
    "evidencestatisticsamplesize_validator",
    "evidencevariable_validator",
    "evidencevariablecategory_validator",
    "evidencevariablecharacteristic_validator",
    "evidencevariablecharacteristicdefinitionbycombination_validator",
    "evidencevariablecharacteristicdefinitionbytypeandvalue_validator",
    "evidencevariablecharacteristictimefromevent_validator",
    "evidencevariabledefinition_validator",
    "examplescenario_validator",
    "examplescenarioactor_validator",
    "examplescenarioinstance_validator",
    "examplescenarioinstancecontainedinstance_validator",
    "examplescenarioinstanceversion_validator",
    "examplescenarioprocess_validator",
    "examplescenarioprocessstep_validator",
    "examplescenarioprocessstepalternative_validator",
    "examplescenarioprocessstepoperation_validator",
    "explanationofbenefit_validator",
    "explanationofbenefitaccident_validator",
    "explanationofbenefitadditem_validator",
    "explanationofbenefitadditembodysite_validator",
    "explanationofbenefitadditemdetail_validator",
    "explanationofbenefitadditemdetailsubdetail_validator",
    "explanationofbenefitbenefitbalance_validator",
    "explanationofbenefitbenefitbalancefinancial_validator",
    "explanationofbenefitcareteam_validator",
    "explanationofbenefitdiagnosis_validator",
    "explanationofbenefitevent_validator",
    "explanationofbenefitinsurance_validator",
    "explanationofbenefititem_validator",
    "explanationofbenefititemadjudication_validator",
    "explanationofbenefititembodysite_validator",
    "explanationofbenefititemdetail_validator",
    "explanationofbenefititemdetailsubdetail_validator",
    "explanationofbenefititemreviewoutcome_validator",
    "explanationofbenefitpayee_validator",
    "explanationofbenefitpayment_validator",
    "explanationofbenefitprocedure_validator",
    "explanationofbenefitprocessnote_validator",
    "explanationofbenefitrelated_validator",
    "explanationofbenefitsupportinginfo_validator",
    "explanationofbenefittotal_validator",
    "expression_validator",
    "extendedcontactdetail_validator",
    "extension_validator",
    "familymemberhistory_validator",
    "familymemberhistorycondition_validator",
    "familymemberhistoryparticipant_validator",
    "familymemberhistoryprocedure_validator",
    "flag_validator",
    "formularyitem_validator",
    "genomicstudy_validator",
    "genomicstudyanalysis_validator",
    "genomicstudyanalysisdevice_validator",
    "genomicstudyanalysisinput_validator",
    "genomicstudyanalysisoutput_validator",
    "genomicstudyanalysisperformer_validator",
    "goal_validator",
    "goaltarget_validator",
    "graphdefinition_validator",
    "graphdefinitionlink_validator",
    "graphdefinitionlinkcompartment_validator",
    "graphdefinitionnode_validator",
    "group_validator",
    "groupcharacteristic_validator",
    "groupmember_validator",
    "guidanceresponse_validator",
    "healthcareservice_validator",
    "healthcareserviceeligibility_validator",
    "humanname_validator",
    "identifier_validator",
    "imagingselection_validator",
    "imagingselectioninstance_validator",
    "imagingselectioninstanceimageregion2d_validator",
    "imagingselectioninstanceimageregion3d_validator",
    "imagingselectionperformer_validator",
    "imagingstudy_validator",
    "imagingstudyseries_validator",
    "imagingstudyseriesinstance_validator",
    "imagingstudyseriesperformer_validator",
    "immunization_validator",
    "immunizationevaluation_validator",
    "immunizationperformer_validator",
    "immunizationprogrameligibility_validator",
    "immunizationprotocolapplied_validator",
    "immunizationreaction_validator",
    "immunizationrecommendation_validator",
    "immunizationrecommendationrecommendation_validator",
    "immunizationrecommendationrecommendationdatecriterion_validator",
    "implementationguide_validator",
    "implementationguidedefinition_validator",
    "implementationguidedefinitiongrouping_validator",
    "implementationguidedefinitionpage_validator",
    "implementationguidedefinitionparameter_validator",
    "implementationguidedefinitionresource_validator",
    "implementationguidedefinitiontemplate_validator",
    "implementationguidedependson_validator",
    "implementationguideglobal_validator",
    "implementationguidemanifest_validator",
    "implementationguidemanifestpage_validator",
    "implementationguidemanifestresource_validator",
    "ingredient_validator",
    "ingredientmanufacturer_validator",
    "ingredientsubstance_validator",
    "ingredientsubstancestrength_validator",
    "ingredientsubstancestrengthreferencestrength_validator",
    "insuranceplan_validator",
    "insuranceplancoverage_validator",
    "insuranceplancoveragebenefit_validator",
    "insuranceplancoveragebenefitlimit_validator",
    "insuranceplanplan_validator",
    "insuranceplanplangeneralcost_validator",
    "insuranceplanplanspecificcost_validator",
    "insuranceplanplanspecificcostbenefit_validator",
    "insuranceplanplanspecificcostbenefitcost_validator",
    "inventoryitem_validator",
    "inventoryitemassociation_validator",
    "inventoryitemcharacteristic_validator",
    "inventoryitemdescription_validator",
    "inventoryiteminstance_validator",
    "inventoryitemname_validator",
    "inventoryitemresponsibleorganization_validator",
    "inventoryreport_validator",
    "inventoryreportinventorylisting_validator",
    "inventoryreportinventorylistingitem_validator",
    "invoice_validator",
    "invoicelineitem_validator",
    "invoiceparticipant_validator",
    "library_validator",
    "linkage_validator",
    "linkageitem_validator",
    "list_validator",
    "listentry_validator",
    "location_validator",
    "locationposition_validator",
    "manufactureditemdefinition_validator",
    "manufactureditemdefinitioncomponent_validator",
    "manufactureditemdefinitioncomponentconstituent_validator",
    "manufactureditemdefinitionproperty_validator",
    "marketingstatus_validator",
    "measure_validator",
    "measuregroup_validator",
    "measuregrouppopulation_validator",
    "measuregroupstratifier_validator",
    "measuregroupstratifiercomponent_validator",
    "measurereport_validator",
    "measurereportgroup_validator",
    "measurereportgrouppopulation_validator",
    "measurereportgroupstratifier_validator",
    "measurereportgroupstratifierstratum_validator",
    "measurereportgroupstratifierstratumcomponent_validator",
    "measurereportgroupstratifierstratumpopulation_validator",
    "measuresupplementaldata_validator",
    "measureterm_validator",
    "medication_validator",
    "medicationadministration_validator",
    "medicationadministrationdosage_validator",
    "medicationadministrationperformer_validator",
    "medicationbatch_validator",
    "medicationdispense_validator",
    "medicationdispenseperformer_validator",
    "medicationdispensesubstitution_validator",
    "medicationingredient_validator",
    "medicationknowledge_validator",
    "medicationknowledgecost_validator",
    "medicationknowledgedefinitional_validator",
    "medicationknowledgedefinitionaldrugcharacteristic_validator",
    "medicationknowledgedefinitionalingredient_validator",
    "medicationknowledgeindicationguideline_validator",
    "medicationknowledgeindicationguidelinedosingguideline_validator",
    "medicationknowledgeindicationguidelinedosingguidelinedosage_validator",
    "medicationknowledgeindicationguidelinedosingguidelinepatientcharacteristic_validator",
    "medicationknowledgemedicineclassification_validator",
    "medicationknowledgemonitoringprogram_validator",
    "medicationknowledgemonograph_validator",
    "medicationknowledgepackaging_validator",
    "medicationknowledgeregulatory_validator",
    "medicationknowledgeregulatorymaxdispense_validator",
    "medicationknowledgeregulatorysubstitution_validator",
    "medicationknowledgerelatedmedicationknowledge_validator",
    "medicationknowledgestorageguideline_validator",
    "medicationknowledgestorageguidelineenvironmentalsetting_validator",
    "medicationrequest_validator",
    "medicationrequestdispenserequest_validator",
    "medicationrequestdispenserequestinitialfill_validator",
    "medicationrequestsubstitution_validator",
    "medicationstatement_validator",
    "medicationstatementadherence_validator",
    "medicinalproductdefinition_validator",
    "medicinalproductdefinitioncharacteristic_validator",
    "medicinalproductdefinitioncontact_validator",
    "medicinalproductdefinitioncrossreference_validator",
    "medicinalproductdefinitionname_validator",
    "medicinalproductdefinitionnamepart_validator",
    "medicinalproductdefinitionnameusage_validator",
    "medicinalproductdefinitionoperation_validator",
    "messagedefinition_validator",
    "messagedefinitionallowedresponse_validator",
    "messagedefinitionfocus_validator",
    "messageheader_validator",
    "messageheaderdestination_validator",
    "messageheaderresponse_validator",
    "messageheadersource_validator",
    "meta_validator",
    "metadataresource_validator",
    "molecularsequence_validator",
    "molecularsequencerelative_validator",
    "molecularsequencerelativeedit_validator",
    "molecularsequencerelativestartingsequence_validator",
    "monetarycomponent_validator",
    "money_validator",
    "namingsystem_validator",
    "namingsystemuniqueid_validator",
    "narrative_validator",
    "nutritionintake_validator",
    "nutritionintakeconsumeditem_validator",
    "nutritionintakeingredientlabel_validator",
    "nutritionintakeperformer_validator",
    "nutritionorder_validator",
    "nutritionorderenteralformula_validator",
    "nutritionorderenteralformulaadditive_validator",
    "nutritionorderenteralformulaadministration_validator",
    "nutritionorderenteralformulaadministrationschedule_validator",
    "nutritionorderoraldiet_validator",
    "nutritionorderoraldietnutrient_validator",
    "nutritionorderoraldietschedule_validator",
    "nutritionorderoraldiettexture_validator",
    "nutritionordersupplement_validator",
    "nutritionordersupplementschedule_validator",
    "nutritionproduct_validator",
    "nutritionproductcharacteristic_validator",
    "nutritionproductingredient_validator",
    "nutritionproductinstance_validator",
    "nutritionproductnutrient_validator",
    "observation_validator",
    "observationcomponent_validator",
    "observationdefinition_validator",
    "observationdefinitioncomponent_validator",
    "observationdefinitionqualifiedvalue_validator",
    "observationreferencerange_validator",
    "observationtriggeredby_validator",
    "operationdefinition_validator",
    "operationdefinitionoverload_validator",
    "operationdefinitionparameter_validator",
    "operationdefinitionparameterbinding_validator",
    "operationdefinitionparameterreferencedfrom_validator",
    "operationoutcome_validator",
    "operationoutcomeissue_validator",
    "organization_validator",
    "organizationaffiliation_validator",
    "organizationqualification_validator",
    "packagedproductdefinition_validator",
    "packagedproductdefinitionlegalstatusofsupply_validator",
    "packagedproductdefinitionpackaging_validator",
    "packagedproductdefinitionpackagingcontaineditem_validator",
    "packagedproductdefinitionpackagingproperty_validator",
    "parameterdefinition_validator",
    "parameters_validator",
    "parametersparameter_validator",
    "patient_validator",
    "patientcommunication_validator",
    "patientcontact_validator",
    "patientlink_validator",
    "paymentnotice_validator",
    "paymentreconciliation_validator",
    "paymentreconciliationallocation_validator",
    "paymentreconciliationprocessnote_validator",
    "period_validator",
    "permission_validator",
    "permissionjustification_validator",
    "permissionrule_validator",
    "permissionruleactivity_validator",
    "permissionruledata_validator",
    "permissionruledataresource_validator",
    "person_validator",
    "personcommunication_validator",
    "personlink_validator",
    "plandefinition_validator",
    "plandefinitionaction_validator",
    "plandefinitionactioncondition_validator",
    "plandefinitionactiondynamicvalue_validator",
    "plandefinitionactioninput_validator",
    "plandefinitionactionoutput_validator",
    "plandefinitionactionparticipant_validator",
    "plandefinitionactionrelatedaction_validator",
    "plandefinitionactor_validator",
    "plandefinitionactoroption_validator",
    "plandefinitiongoal_validator",
    "plandefinitiongoaltarget_validator",
    "practitioner_validator",
    "practitionercommunication_validator",
    "practitionerqualification_validator",
    "practitionerrole_validator",
    "primitivetype_validator",
    "procedure_validator",
    "procedurefocaldevice_validator",
    "procedureperformer_validator",
    "productshelflife_validator",
    "provenance_validator",
    "provenanceagent_validator",
    "provenanceentity_validator",
    "quantity_validator",
    "questionnaire_validator",
    "questionnaireitem_validator",
    "questionnaireitemansweroption_validator",
    "questionnaireitemenablewhen_validator",
    "questionnaireiteminitial_validator",
    "questionnaireresponse_validator",
    "questionnaireresponseitem_validator",
    "questionnaireresponseitemanswer_validator",
    "range_validator",
    "ratio_validator",
    "ratiorange_validator",
    "reference_validator",
    "regulatedauthorization_validator",
    "regulatedauthorizationcase_validator",
    "relatedartifact_validator",
    "relatedperson_validator",
    "relatedpersoncommunication_validator",
    "requestorchestration_validator",
    "requestorchestrationaction_validator",
    "requestorchestrationactioncondition_validator",
    "requestorchestrationactiondynamicvalue_validator",
    "requestorchestrationactioninput_validator",
    "requestorchestrationactionoutput_validator",
    "requestorchestrationactionparticipant_validator",
    "requestorchestrationactionrelatedaction_validator",
    "requirements_validator",
    "requirementsstatement_validator",
    "researchstudy_validator",
    "researchstudyassociatedparty_validator",
    "researchstudycomparisongroup_validator",
    "researchstudylabel_validator",
    "researchstudyobjective_validator",
    "researchstudyoutcomemeasure_validator",
    "researchstudyprogressstatus_validator",
    "researchstudyrecruitment_validator",
    "researchsubject_validator",
    "researchsubjectprogress_validator",
    "resource_validator",
    "riskassessment_validator",
    "riskassessmentprediction_validator",
    "sampleddata_validator",
    "schedule_validator",
    "searchparameter_validator",
    "searchparametercomponent_validator",
    "servicerequest_validator",
    "servicerequestorderdetail_validator",
    "servicerequestorderdetailparameter_validator",
    "servicerequestpatientinstruction_validator",
    "signature_validator",
    "slot_validator",
    "specimen_validator",
    "specimencollection_validator",
    "specimencontainer_validator",
    "specimendefinition_validator",
    "specimendefinitiontypetested_validator",
    "specimendefinitiontypetestedcontainer_validator",
    "specimendefinitiontypetestedcontaineradditive_validator",
    "specimendefinitiontypetestedhandling_validator",
    "specimenfeature_validator",
    "specimenprocessing_validator",
    "structuredefinition_validator",
    "structuredefinitioncontext_validator",
    "structuredefinitiondifferential_validator",
    "structuredefinitionmapping_validator",
    "structuredefinitionsnapshot_validator",
    "structuremap_validator",
    "structuremapconst_validator",
    "structuremapgroup_validator",
    "structuremapgroupinput_validator",
    "structuremapgrouprule_validator",
    "structuremapgroupruledependent_validator",
    "structuremapgrouprulesource_validator",
    "structuremapgroupruletarget_validator",
    "structuremapgroupruletargetparameter_validator",
    "structuremapstructure_validator",
    "subscription_validator",
    "subscriptionfilterby_validator",
    "subscriptionparameter_validator",
    "subscriptionstatus_validator",
    "subscriptionstatusnotificationevent_validator",
    "subscriptiontopic_validator",
    "subscriptiontopiccanfilterby_validator",
    "subscriptiontopiceventtrigger_validator",
    "subscriptiontopicnotificationshape_validator",
    "subscriptiontopicresourcetrigger_validator",
    "subscriptiontopicresourcetriggerquerycriteria_validator",
    "substance_validator",
    "substancedefinition_validator",
    "substancedefinitioncharacterization_validator",
    "substancedefinitioncode_validator",
    "substancedefinitionmoiety_validator",
    "substancedefinitionmolecularweight_validator",
    "substancedefinitionname_validator",
    "substancedefinitionnameofficial_validator",
    "substancedefinitionproperty_validator",
    "substancedefinitionrelationship_validator",
    "substancedefinitionsourcematerial_validator",
    "substancedefinitionstructure_validator",
    "substancedefinitionstructurerepresentation_validator",
    "substanceingredient_validator",
    "substancenucleicacid_validator",
    "substancenucleicacidsubunit_validator",
    "substancenucleicacidsubunitlinkage_validator",
    "substancenucleicacidsubunitsugar_validator",
    "substancepolymer_validator",
    "substancepolymermonomerset_validator",
    "substancepolymermonomersetstartingmaterial_validator",
    "substancepolymerrepeat_validator",
    "substancepolymerrepeatrepeatunit_validator",
    "substancepolymerrepeatrepeatunitdegreeofpolymerisation_validator",
    "substancepolymerrepeatrepeatunitstructuralrepresentation_validator",
    "substanceprotein_validator",
    "substanceproteinsubunit_validator",
    "substancereferenceinformation_validator",
    "substancereferenceinformationgene_validator",
    "substancereferenceinformationgeneelement_validator",
    "substancereferenceinformationtarget_validator",
    "substancesourcematerial_validator",
    "substancesourcematerialfractiondescription_validator",
    "substancesourcematerialorganism_validator",
    "substancesourcematerialorganismauthor_validator",
    "substancesourcematerialorganismhybrid_validator",
    "substancesourcematerialorganismorganismgeneral_validator",
    "substancesourcematerialpartdescription_validator",
    "supplydelivery_validator",
    "supplydeliverysupplieditem_validator",
    "supplyrequest_validator",
    "supplyrequestparameter_validator",
    "task_validator",
    "taskinput_validator",
    "taskoutput_validator",
    "taskperformer_validator",
    "taskrestriction_validator",
    "terminologycapabilities_validator",
    "terminologycapabilitiesclosure_validator",
    "terminologycapabilitiescodesystem_validator",
    "terminologycapabilitiescodesystemversion_validator",
    "terminologycapabilitiescodesystemversionfilter_validator",
    "terminologycapabilitiesexpansion_validator",
    "terminologycapabilitiesexpansionparameter_validator",
    "terminologycapabilitiesimplementation_validator",
    "terminologycapabilitiessoftware_validator",
    "terminologycapabilitiestranslation_validator",
    "terminologycapabilitiesvalidatecode_validator",
    "testplan_validator",
    "testplandependency_validator",
    "testplantestcase_validator",
    "testplantestcaseassertion_validator",
    "testplantestcasedependency_validator",
    "testplantestcasetestdata_validator",
    "testplantestcasetestrun_validator",
    "testplantestcasetestrunscript_validator",
    "testreport_validator",
    "testreportparticipant_validator",
    "testreportsetup_validator",
    "testreportsetupaction_validator",
    "testreportsetupactionassert_validator",
    "testreportsetupactionassertrequirement_validator",
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
    "testscriptscope_validator",
    "testscriptsetup_validator",
    "testscriptsetupaction_validator",
    "testscriptsetupactionassert_validator",
    "testscriptsetupactionassertrequirement_validator",
    "testscriptsetupactionoperation_validator",
    "testscriptsetupactionoperationrequestheader_validator",
    "testscriptteardown_validator",
    "testscriptteardownaction_validator",
    "testscripttest_validator",
    "testscripttestaction_validator",
    "testscriptvariable_validator",
    "timing_validator",
    "timingrepeat_validator",
    "transport_validator",
    "transportinput_validator",
    "transportoutput_validator",
    "transportrestriction_validator",
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
    "valuesetexpansioncontainsproperty_validator",
    "valuesetexpansioncontainspropertysubproperty_validator",
    "valuesetexpansionparameter_validator",
    "valuesetexpansionproperty_validator",
    "valuesetscope_validator",
    "verificationresult_validator",
    "verificationresultattestation_validator",
    "verificationresultprimarysource_validator",
    "verificationresultvalidator_validator",
    "virtualservicedetail_validator",
    "visionprescription_validator",
    "visionprescriptionlensspecification_validator",
    "visionprescriptionlensspecificationprism_validator",
]
