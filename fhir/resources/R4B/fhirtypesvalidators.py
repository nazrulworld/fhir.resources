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
    "AdverseEventSuspectEntity": (None, ".adverseevent"),
    "AdverseEventSuspectEntityCausality": (None, ".adverseevent"),
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
    "BiologicallyDerivedProduct": (None, ".biologicallyderivedproduct"),
    "BiologicallyDerivedProductCollection": (None, ".biologicallyderivedproduct"),
    "BiologicallyDerivedProductManipulation": (None, ".biologicallyderivedproduct"),
    "BiologicallyDerivedProductProcessing": (None, ".biologicallyderivedproduct"),
    "BiologicallyDerivedProductStorage": (None, ".biologicallyderivedproduct"),
    "BodyStructure": (None, ".bodystructure"),
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
    "CarePlanActivityDetail": (None, ".careplan"),
    "CareTeam": (None, ".careteam"),
    "CareTeamParticipant": (None, ".careteam"),
    "CatalogEntry": (None, ".catalogentry"),
    "CatalogEntryRelatedEntry": (None, ".catalogentry"),
    "ChargeItem": (None, ".chargeitem"),
    "ChargeItemDefinition": (None, ".chargeitemdefinition"),
    "ChargeItemDefinitionApplicability": (None, ".chargeitemdefinition"),
    "ChargeItemDefinitionPropertyGroup": (None, ".chargeitemdefinition"),
    "ChargeItemDefinitionPropertyGroupPriceComponent": (None, ".chargeitemdefinition"),
    "ChargeItemPerformer": (None, ".chargeitem"),
    "Citation": (None, ".citation"),
    "CitationCitedArtifact": (None, ".citation"),
    "CitationCitedArtifactAbstract": (None, ".citation"),
    "CitationCitedArtifactClassification": (None, ".citation"),
    "CitationCitedArtifactClassificationWhoClassified": (None, ".citation"),
    "CitationCitedArtifactContributorship": (None, ".citation"),
    "CitationCitedArtifactContributorshipEntry": (None, ".citation"),
    "CitationCitedArtifactContributorshipEntryAffiliationInfo": (None, ".citation"),
    "CitationCitedArtifactContributorshipEntryContributionInstance": (
        None,
        ".citation",
    ),
    "CitationCitedArtifactContributorshipSummary": (None, ".citation"),
    "CitationCitedArtifactPart": (None, ".citation"),
    "CitationCitedArtifactPublicationForm": (None, ".citation"),
    "CitationCitedArtifactPublicationFormPeriodicRelease": (None, ".citation"),
    "CitationCitedArtifactPublicationFormPeriodicReleaseDateOfPublication": (
        None,
        ".citation",
    ),
    "CitationCitedArtifactPublicationFormPublishedIn": (None, ".citation"),
    "CitationCitedArtifactRelatesTo": (None, ".citation"),
    "CitationCitedArtifactStatusDate": (None, ".citation"),
    "CitationCitedArtifactTitle": (None, ".citation"),
    "CitationCitedArtifactVersion": (None, ".citation"),
    "CitationCitedArtifactWebLocation": (None, ".citation"),
    "CitationClassification": (None, ".citation"),
    "CitationRelatesTo": (None, ".citation"),
    "CitationStatusDate": (None, ".citation"),
    "CitationSummary": (None, ".citation"),
    "Claim": (None, ".claim"),
    "ClaimAccident": (None, ".claim"),
    "ClaimCareTeam": (None, ".claim"),
    "ClaimDiagnosis": (None, ".claim"),
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
    "ClaimResponseAddItemDetailSubDetail": (None, ".claimresponse"),
    "ClaimResponseError": (None, ".claimresponse"),
    "ClaimResponseInsurance": (None, ".claimresponse"),
    "ClaimResponseItem": (None, ".claimresponse"),
    "ClaimResponseItemAdjudication": (None, ".claimresponse"),
    "ClaimResponseItemDetail": (None, ".claimresponse"),
    "ClaimResponseItemDetailSubDetail": (None, ".claimresponse"),
    "ClaimResponsePayment": (None, ".claimresponse"),
    "ClaimResponseProcessNote": (None, ".claimresponse"),
    "ClaimResponseTotal": (None, ".claimresponse"),
    "ClaimSupportingInfo": (None, ".claim"),
    "ClinicalImpression": (None, ".clinicalimpression"),
    "ClinicalImpressionFinding": (None, ".clinicalimpression"),
    "ClinicalImpressionInvestigation": (None, ".clinicalimpression"),
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
    "ConsentPolicy": (None, ".consent"),
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
    "CoverageEligibilityRequestInsurance": (None, ".coverageeligibilityrequest"),
    "CoverageEligibilityRequestItem": (None, ".coverageeligibilityrequest"),
    "CoverageEligibilityRequestItemDiagnosis": (None, ".coverageeligibilityrequest"),
    "CoverageEligibilityRequestSupportingInfo": (None, ".coverageeligibilityrequest"),
    "CoverageEligibilityResponse": (None, ".coverageeligibilityresponse"),
    "CoverageEligibilityResponseError": (None, ".coverageeligibilityresponse"),
    "CoverageEligibilityResponseInsurance": (None, ".coverageeligibilityresponse"),
    "CoverageEligibilityResponseInsuranceItem": (None, ".coverageeligibilityresponse"),
    "CoverageEligibilityResponseInsuranceItemBenefit": (
        None,
        ".coverageeligibilityresponse",
    ),
    "DataRequirement": (None, ".datarequirement"),
    "DataRequirementCodeFilter": (None, ".datarequirement"),
    "DataRequirementDateFilter": (None, ".datarequirement"),
    "DataRequirementSort": (None, ".datarequirement"),
    "DetectedIssue": (None, ".detectedissue"),
    "DetectedIssueEvidence": (None, ".detectedissue"),
    "DetectedIssueMitigation": (None, ".detectedissue"),
    "Device": (None, ".device"),
    "DeviceDefinition": (None, ".devicedefinition"),
    "DeviceDefinitionCapability": (None, ".devicedefinition"),
    "DeviceDefinitionDeviceName": (None, ".devicedefinition"),
    "DeviceDefinitionMaterial": (None, ".devicedefinition"),
    "DeviceDefinitionProperty": (None, ".devicedefinition"),
    "DeviceDefinitionSpecialization": (None, ".devicedefinition"),
    "DeviceDefinitionUdiDeviceIdentifier": (None, ".devicedefinition"),
    "DeviceDeviceName": (None, ".device"),
    "DeviceMetric": (None, ".devicemetric"),
    "DeviceMetricCalibration": (None, ".devicemetric"),
    "DeviceProperty": (None, ".device"),
    "DeviceRequest": (None, ".devicerequest"),
    "DeviceRequestParameter": (None, ".devicerequest"),
    "DeviceSpecialization": (None, ".device"),
    "DeviceUdiCarrier": (None, ".device"),
    "DeviceUseStatement": (None, ".deviceusestatement"),
    "DeviceVersion": (None, ".device"),
    "DiagnosticReport": (None, ".diagnosticreport"),
    "DiagnosticReportMedia": (None, ".diagnosticreport"),
    "Distance": (None, ".distance"),
    "DocumentManifest": (None, ".documentmanifest"),
    "DocumentManifestRelated": (None, ".documentmanifest"),
    "DocumentReference": (None, ".documentreference"),
    "DocumentReferenceContent": (None, ".documentreference"),
    "DocumentReferenceContext": (None, ".documentreference"),
    "DocumentReferenceRelatesTo": (None, ".documentreference"),
    "DomainResource": (None, ".domainresource"),
    "Dosage": (None, ".dosage"),
    "DosageDoseAndRate": (None, ".dosage"),
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
    "EventDefinition": (None, ".eventdefinition"),
    "Evidence": (None, ".evidence"),
    "EvidenceCertainty": (None, ".evidence"),
    "EvidenceReport": (None, ".evidencereport"),
    "EvidenceReportRelatesTo": (None, ".evidencereport"),
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
    "EvidenceVariableCharacteristicTimeFromStart": (None, ".evidencevariable"),
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
    "ExplanationOfBenefitAddItemDetail": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitAddItemDetailSubDetail": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitBenefitBalance": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitBenefitBalanceFinancial": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitCareTeam": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitDiagnosis": (None, ".explanationofbenefit"),
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
    "ExplanationOfBenefitSupportingInfo": (None, ".explanationofbenefit"),
    "ExplanationOfBenefitTotal": (None, ".explanationofbenefit"),
    "Expression": (None, ".expression"),
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
    "HealthcareServiceEligibility": (None, ".healthcareservice"),
    "HealthcareServiceNotAvailable": (None, ".healthcareservice"),
    "HumanName": (None, ".humanname"),
    "Identifier": (None, ".identifier"),
    "ImagingStudy": (None, ".imagingstudy"),
    "ImagingStudySeries": (None, ".imagingstudy"),
    "ImagingStudySeriesInstance": (None, ".imagingstudy"),
    "ImagingStudySeriesPerformer": (None, ".imagingstudy"),
    "Immunization": (None, ".immunization"),
    "ImmunizationEducation": (None, ".immunization"),
    "ImmunizationEvaluation": (None, ".immunizationevaluation"),
    "ImmunizationPerformer": (None, ".immunization"),
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
    "InsurancePlanContact": (None, ".insuranceplan"),
    "InsurancePlanCoverage": (None, ".insuranceplan"),
    "InsurancePlanCoverageBenefit": (None, ".insuranceplan"),
    "InsurancePlanCoverageBenefitLimit": (None, ".insuranceplan"),
    "InsurancePlanPlan": (None, ".insuranceplan"),
    "InsurancePlanPlanGeneralCost": (None, ".insuranceplan"),
    "InsurancePlanPlanSpecificCost": (None, ".insuranceplan"),
    "InsurancePlanPlanSpecificCostBenefit": (None, ".insuranceplan"),
    "InsurancePlanPlanSpecificCostBenefitCost": (None, ".insuranceplan"),
    "Invoice": (None, ".invoice"),
    "InvoiceLineItem": (None, ".invoice"),
    "InvoiceLineItemPriceComponent": (None, ".invoice"),
    "InvoiceParticipant": (None, ".invoice"),
    "Library": (None, ".library"),
    "Linkage": (None, ".linkage"),
    "LinkageItem": (None, ".linkage"),
    "List": (None, ".list"),
    "ListEntry": (None, ".list"),
    "Location": (None, ".location"),
    "LocationHoursOfOperation": (None, ".location"),
    "LocationPosition": (None, ".location"),
    "ManufacturedItemDefinition": (None, ".manufactureditemdefinition"),
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
    "Media": (None, ".media"),
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
    "MedicationKnowledgeAdministrationGuidelines": (None, ".medicationknowledge"),
    "MedicationKnowledgeAdministrationGuidelinesDosage": (None, ".medicationknowledge"),
    "MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics": (
        None,
        ".medicationknowledge",
    ),
    "MedicationKnowledgeCost": (None, ".medicationknowledge"),
    "MedicationKnowledgeDrugCharacteristic": (None, ".medicationknowledge"),
    "MedicationKnowledgeIngredient": (None, ".medicationknowledge"),
    "MedicationKnowledgeKinetics": (None, ".medicationknowledge"),
    "MedicationKnowledgeMedicineClassification": (None, ".medicationknowledge"),
    "MedicationKnowledgeMonitoringProgram": (None, ".medicationknowledge"),
    "MedicationKnowledgeMonograph": (None, ".medicationknowledge"),
    "MedicationKnowledgePackaging": (None, ".medicationknowledge"),
    "MedicationKnowledgeRegulatory": (None, ".medicationknowledge"),
    "MedicationKnowledgeRegulatoryMaxDispense": (None, ".medicationknowledge"),
    "MedicationKnowledgeRegulatorySchedule": (None, ".medicationknowledge"),
    "MedicationKnowledgeRegulatorySubstitution": (None, ".medicationknowledge"),
    "MedicationKnowledgeRelatedMedicationKnowledge": (None, ".medicationknowledge"),
    "MedicationRequest": (None, ".medicationrequest"),
    "MedicationRequestDispenseRequest": (None, ".medicationrequest"),
    "MedicationRequestDispenseRequestInitialFill": (None, ".medicationrequest"),
    "MedicationRequestSubstitution": (None, ".medicationrequest"),
    "MedicationStatement": (None, ".medicationstatement"),
    "MedicinalProductDefinition": (None, ".medicinalproductdefinition"),
    "MedicinalProductDefinitionCharacteristic": (None, ".medicinalproductdefinition"),
    "MedicinalProductDefinitionContact": (None, ".medicinalproductdefinition"),
    "MedicinalProductDefinitionCrossReference": (None, ".medicinalproductdefinition"),
    "MedicinalProductDefinitionName": (None, ".medicinalproductdefinition"),
    "MedicinalProductDefinitionNameCountryLanguage": (
        None,
        ".medicinalproductdefinition",
    ),
    "MedicinalProductDefinitionNameNamePart": (None, ".medicinalproductdefinition"),
    "MedicinalProductDefinitionOperation": (None, ".medicinalproductdefinition"),
    "MessageDefinition": (None, ".messagedefinition"),
    "MessageDefinitionAllowedResponse": (None, ".messagedefinition"),
    "MessageDefinitionFocus": (None, ".messagedefinition"),
    "MessageHeader": (None, ".messageheader"),
    "MessageHeaderDestination": (None, ".messageheader"),
    "MessageHeaderResponse": (None, ".messageheader"),
    "MessageHeaderSource": (None, ".messageheader"),
    "Meta": (None, ".meta"),
    "MolecularSequence": (None, ".molecularsequence"),
    "MolecularSequenceQuality": (None, ".molecularsequence"),
    "MolecularSequenceQualityRoc": (None, ".molecularsequence"),
    "MolecularSequenceReferenceSeq": (None, ".molecularsequence"),
    "MolecularSequenceRepository": (None, ".molecularsequence"),
    "MolecularSequenceStructureVariant": (None, ".molecularsequence"),
    "MolecularSequenceStructureVariantInner": (None, ".molecularsequence"),
    "MolecularSequenceStructureVariantOuter": (None, ".molecularsequence"),
    "MolecularSequenceVariant": (None, ".molecularsequence"),
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
    "NutritionProduct": (None, ".nutritionproduct"),
    "NutritionProductIngredient": (None, ".nutritionproduct"),
    "NutritionProductInstance": (None, ".nutritionproduct"),
    "NutritionProductNutrient": (None, ".nutritionproduct"),
    "NutritionProductProductCharacteristic": (None, ".nutritionproduct"),
    "Observation": (None, ".observation"),
    "ObservationComponent": (None, ".observation"),
    "ObservationDefinition": (None, ".observationdefinition"),
    "ObservationDefinitionQualifiedInterval": (None, ".observationdefinition"),
    "ObservationDefinitionQuantitativeDetails": (None, ".observationdefinition"),
    "ObservationReferenceRange": (None, ".observation"),
    "OperationDefinition": (None, ".operationdefinition"),
    "OperationDefinitionOverload": (None, ".operationdefinition"),
    "OperationDefinitionParameter": (None, ".operationdefinition"),
    "OperationDefinitionParameterBinding": (None, ".operationdefinition"),
    "OperationDefinitionParameterReferencedFrom": (None, ".operationdefinition"),
    "OperationOutcome": (None, ".operationoutcome"),
    "OperationOutcomeIssue": (None, ".operationoutcome"),
    "Organization": (None, ".organization"),
    "OrganizationAffiliation": (None, ".organizationaffiliation"),
    "OrganizationContact": (None, ".organization"),
    "PackagedProductDefinition": (None, ".packagedproductdefinition"),
    "PackagedProductDefinitionLegalStatusOfSupply": (
        None,
        ".packagedproductdefinition",
    ),
    "PackagedProductDefinitionPackage": (None, ".packagedproductdefinition"),
    "PackagedProductDefinitionPackageContainedItem": (
        None,
        ".packagedproductdefinition",
    ),
    "PackagedProductDefinitionPackageProperty": (None, ".packagedproductdefinition"),
    "PackagedProductDefinitionPackageShelfLifeStorage": (
        None,
        ".packagedproductdefinition",
    ),
    "ParameterDefinition": (None, ".parameterdefinition"),
    "Parameters": (None, ".parameters"),
    "ParametersParameter": (None, ".parameters"),
    "Patient": (None, ".patient"),
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
    "Population": (None, ".population"),
    "Practitioner": (None, ".practitioner"),
    "PractitionerQualification": (None, ".practitioner"),
    "PractitionerRole": (None, ".practitionerrole"),
    "PractitionerRoleAvailableTime": (None, ".practitionerrole"),
    "PractitionerRoleNotAvailable": (None, ".practitionerrole"),
    "Procedure": (None, ".procedure"),
    "ProcedureFocalDevice": (None, ".procedure"),
    "ProcedurePerformer": (None, ".procedure"),
    "ProdCharacteristic": (None, ".prodcharacteristic"),
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
    "RequestGroup": (None, ".requestgroup"),
    "RequestGroupAction": (None, ".requestgroup"),
    "RequestGroupActionCondition": (None, ".requestgroup"),
    "RequestGroupActionRelatedAction": (None, ".requestgroup"),
    "ResearchDefinition": (None, ".researchdefinition"),
    "ResearchElementDefinition": (None, ".researchelementdefinition"),
    "ResearchElementDefinitionCharacteristic": (None, ".researchelementdefinition"),
    "ResearchStudy": (None, ".researchstudy"),
    "ResearchStudyArm": (None, ".researchstudy"),
    "ResearchStudyObjective": (None, ".researchstudy"),
    "ResearchSubject": (None, ".researchsubject"),
    "Resource": (None, ".resource"),
    "RiskAssessment": (None, ".riskassessment"),
    "RiskAssessmentPrediction": (None, ".riskassessment"),
    "SampledData": (None, ".sampleddata"),
    "Schedule": (None, ".schedule"),
    "SearchParameter": (None, ".searchparameter"),
    "SearchParameterComponent": (None, ".searchparameter"),
    "ServiceRequest": (None, ".servicerequest"),
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
    "SpecimenProcessing": (None, ".specimen"),
    "StructureDefinition": (None, ".structuredefinition"),
    "StructureDefinitionContext": (None, ".structuredefinition"),
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
    "SubstanceInstance": (None, ".substance"),
    "SupplyDelivery": (None, ".supplydelivery"),
    "SupplyDeliverySuppliedItem": (None, ".supplydelivery"),
    "SupplyRequest": (None, ".supplyrequest"),
    "SupplyRequestParameter": (None, ".supplyrequest"),
    "Task": (None, ".task"),
    "TaskInput": (None, ".task"),
    "TaskOutput": (None, ".task"),
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
    "TestScriptSetup": (None, ".testscript"),
    "TestScriptSetupAction": (None, ".testscript"),
    "TestScriptSetupActionAssert": (None, ".testscript"),
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
    "VerificationResult": (None, ".verificationresult"),
    "VerificationResultAttestation": (None, ".verificationresult"),
    "VerificationResultPrimarySource": (None, ".verificationresult"),
    "VerificationResultValidator": (None, ".verificationresult"),
    "VisionPrescription": (None, ".visionprescription"),
    "VisionPrescriptionLensSpecification": (None, ".visionprescription"),
    "VisionPrescriptionLensSpecificationPrism": (None, ".visionprescription"),
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


def biologicallyderivedproduct_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("BiologicallyDerivedProduct", v)


def biologicallyderivedproductcollection_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("BiologicallyDerivedProductCollection", v)


def biologicallyderivedproductmanipulation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("BiologicallyDerivedProductManipulation", v)


def biologicallyderivedproductprocessing_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("BiologicallyDerivedProductProcessing", v)


def biologicallyderivedproductstorage_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("BiologicallyDerivedProductStorage", v)


def bodystructure_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("BodyStructure", v)


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


def careplanactivitydetail_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CarePlanActivityDetail", v)


def careteam_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CareTeam", v)


def careteamparticipant_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CareTeamParticipant", v)


def catalogentry_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CatalogEntry", v)


def catalogentryrelatedentry_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CatalogEntryRelatedEntry", v)


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


def chargeitemdefinitionpropertygrouppricecomponent_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ChargeItemDefinitionPropertyGroupPriceComponent", v)


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


def citationcitedartifactclassificationwhoclassified_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CitationCitedArtifactClassificationWhoClassified", v)


def citationcitedartifactcontributorship_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CitationCitedArtifactContributorship", v)


def citationcitedartifactcontributorshipentry_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("CitationCitedArtifactContributorshipEntry", v)


def citationcitedartifactcontributorshipentryaffiliationinfo_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator(
        "CitationCitedArtifactContributorshipEntryAffiliationInfo", v
    )


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


def citationcitedartifactpublicationformperiodicrelease_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator(
        "CitationCitedArtifactPublicationFormPeriodicRelease", v
    )


def citationcitedartifactpublicationformperiodicreleasedateofpublication_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator(
        "CitationCitedArtifactPublicationFormPeriodicReleaseDateOfPublication", v
    )


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


def citationrelatesto_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CitationRelatesTo", v)


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


def claimresponseadditemdetailsubdetail_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClaimResponseAddItemDetailSubDetail", v)


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


def clinicalimpressioninvestigation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ClinicalImpressionInvestigation", v)


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


def consentpolicy_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ConsentPolicy", v)


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


def devicedefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceDefinition", v)


def devicedefinitioncapability_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceDefinitionCapability", v)


def devicedefinitiondevicename_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceDefinitionDeviceName", v)


def devicedefinitionmaterial_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceDefinitionMaterial", v)


def devicedefinitionproperty_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceDefinitionProperty", v)


def devicedefinitionspecialization_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceDefinitionSpecialization", v)


def devicedefinitionudideviceidentifier_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceDefinitionUdiDeviceIdentifier", v)


def devicedevicename_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceDeviceName", v)


def devicemetric_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceMetric", v)


def devicemetriccalibration_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("DeviceMetricCalibration", v)


def deviceproperty_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceProperty", v)


def devicerequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceRequest", v)


def devicerequestparameter_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceRequestParameter", v)


def devicespecialization_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceSpecialization", v)


def deviceudicarrier_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceUdiCarrier", v)


def deviceusestatement_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceUseStatement", v)


def deviceversion_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DeviceVersion", v)


def diagnosticreport_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DiagnosticReport", v)


def diagnosticreportmedia_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DiagnosticReportMedia", v)


def distance_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Distance", v)


def documentmanifest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("DocumentManifest", v)


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


def evidencevariablecharacteristictimefromstart_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("EvidenceVariableCharacteristicTimeFromStart", v)


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


def healthcareserviceeligibility_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("HealthcareServiceEligibility", v)


def healthcareservicenotavailable_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("HealthcareServiceNotAvailable", v)


def humanname_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("HumanName", v)


def identifier_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Identifier", v)


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


def immunizationeducation_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ImmunizationEducation", v)


def immunizationevaluation_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ImmunizationEvaluation", v)


def immunizationperformer_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ImmunizationPerformer", v)


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


def insuranceplancontact_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("InsurancePlanContact", v)


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


def invoice_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Invoice", v)


def invoicelineitem_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("InvoiceLineItem", v)


def invoicelineitempricecomponent_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("InvoiceLineItemPriceComponent", v)


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


def locationhoursofoperation_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("LocationHoursOfOperation", v)


def locationposition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("LocationPosition", v)


def manufactureditemdefinition_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ManufacturedItemDefinition", v)


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


def medicationknowledgeadministrationguidelines_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationKnowledgeAdministrationGuidelines", v)


def medicationknowledgeadministrationguidelinesdosage_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationKnowledgeAdministrationGuidelinesDosage", v)


def medicationknowledgeadministrationguidelinespatientcharacteristics_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator(
        "MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics", v
    )


def medicationknowledgecost_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationKnowledgeCost", v)


def medicationknowledgedrugcharacteristic_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationKnowledgeDrugCharacteristic", v)


def medicationknowledgeingredient_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationKnowledgeIngredient", v)


def medicationknowledgekinetics_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationKnowledgeKinetics", v)


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


def medicationknowledgeregulatoryschedule_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationKnowledgeRegulatorySchedule", v)


def medicationknowledgeregulatorysubstitution_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationKnowledgeRegulatorySubstitution", v)


def medicationknowledgerelatedmedicationknowledge_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicationKnowledgeRelatedMedicationKnowledge", v)


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


def medicinalproductdefinitionnamecountrylanguage_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicinalProductDefinitionNameCountryLanguage", v)


def medicinalproductdefinitionnamenamepart_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MedicinalProductDefinitionNameNamePart", v)


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


def molecularsequence_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("MolecularSequence", v)


def molecularsequencequality_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MolecularSequenceQuality", v)


def molecularsequencequalityroc_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MolecularSequenceQualityRoc", v)


def molecularsequencereferenceseq_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MolecularSequenceReferenceSeq", v)


def molecularsequencerepository_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MolecularSequenceRepository", v)


def molecularsequencestructurevariant_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MolecularSequenceStructureVariant", v)


def molecularsequencestructurevariantinner_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MolecularSequenceStructureVariantInner", v)


def molecularsequencestructurevariantouter_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MolecularSequenceStructureVariantOuter", v)


def molecularsequencevariant_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("MolecularSequenceVariant", v)


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


def nutritionproduct_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("NutritionProduct", v)


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


def nutritionproductproductcharacteristic_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("NutritionProductProductCharacteristic", v)


def observation_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Observation", v)


def observationcomponent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ObservationComponent", v)


def observationdefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ObservationDefinition", v)


def observationdefinitionqualifiedinterval_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ObservationDefinitionQualifiedInterval", v)


def observationdefinitionquantitativedetails_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ObservationDefinitionQuantitativeDetails", v)


def observationreferencerange_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ObservationReferenceRange", v)


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


def organizationcontact_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("OrganizationContact", v)


def packagedproductdefinition_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PackagedProductDefinition", v)


def packagedproductdefinitionlegalstatusofsupply_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PackagedProductDefinitionLegalStatusOfSupply", v)


def packagedproductdefinitionpackage_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PackagedProductDefinitionPackage", v)


def packagedproductdefinitionpackagecontaineditem_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PackagedProductDefinitionPackageContainedItem", v)


def packagedproductdefinitionpackageproperty_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PackagedProductDefinitionPackageProperty", v)


def packagedproductdefinitionpackageshelflifestorage_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("PackagedProductDefinitionPackageShelfLifeStorage", v)


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


def population_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Population", v)


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


def prodcharacteristic_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ProdCharacteristic", v)


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


def researchdefinition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ResearchDefinition", v)


def researchelementdefinition_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ResearchElementDefinition", v)


def researchelementdefinitioncharacteristic_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("ResearchElementDefinitionCharacteristic", v)


def researchstudy_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ResearchStudy", v)


def researchstudyarm_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ResearchStudyArm", v)


def researchstudyobjective_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ResearchStudyObjective", v)


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


def servicerequest_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ServiceRequest", v)


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


def supplyrequestparameter_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SupplyRequestParameter", v)


def task_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Task", v)


def taskinput_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TaskInput", v)


def taskoutput_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TaskOutput", v)


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


def testscriptsetup_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptSetup", v)


def testscriptsetupaction_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TestScriptSetupAction", v)


def testscriptsetupactionassert_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("TestScriptSetupActionAssert", v)


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
    "accountcoverage_validator",
    "accountguarantor_validator",
    "activitydefinition_validator",
    "activitydefinitiondynamicvalue_validator",
    "activitydefinitionparticipant_validator",
    "address_validator",
    "administrableproductdefinition_validator",
    "administrableproductdefinitionproperty_validator",
    "administrableproductdefinitionrouteofadministration_validator",
    "administrableproductdefinitionrouteofadministrationtargetspecies_validator",
    "administrableproductdefinitionrouteofadministrationtargetspecieswithdrawalperiod_validator",  # noqa: B950
    "adverseevent_validator",
    "adverseeventsuspectentity_validator",
    "adverseeventsuspectentitycausality_validator",
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
    "biologicallyderivedproduct_validator",
    "biologicallyderivedproductcollection_validator",
    "biologicallyderivedproductmanipulation_validator",
    "biologicallyderivedproductprocessing_validator",
    "biologicallyderivedproductstorage_validator",
    "bodystructure_validator",
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
    "careplanactivitydetail_validator",
    "careteam_validator",
    "careteamparticipant_validator",
    "catalogentry_validator",
    "catalogentryrelatedentry_validator",
    "chargeitem_validator",
    "chargeitemdefinition_validator",
    "chargeitemdefinitionapplicability_validator",
    "chargeitemdefinitionpropertygroup_validator",
    "chargeitemdefinitionpropertygrouppricecomponent_validator",
    "chargeitemperformer_validator",
    "citation_validator",
    "citationcitedartifact_validator",
    "citationcitedartifactabstract_validator",
    "citationcitedartifactclassification_validator",
    "citationcitedartifactclassificationwhoclassified_validator",
    "citationcitedartifactcontributorship_validator",
    "citationcitedartifactcontributorshipentry_validator",
    "citationcitedartifactcontributorshipentryaffiliationinfo_validator",
    "citationcitedartifactcontributorshipentrycontributioninstance_validator",
    "citationcitedartifactcontributorshipsummary_validator",
    "citationcitedartifactpart_validator",
    "citationcitedartifactpublicationform_validator",
    "citationcitedartifactpublicationformperiodicrelease_validator",
    "citationcitedartifactpublicationformperiodicreleasedateofpublication_validator",
    "citationcitedartifactpublicationformpublishedin_validator",
    "citationcitedartifactrelatesto_validator",
    "citationcitedartifactstatusdate_validator",
    "citationcitedartifacttitle_validator",
    "citationcitedartifactversion_validator",
    "citationcitedartifactweblocation_validator",
    "citationclassification_validator",
    "citationrelatesto_validator",
    "citationstatusdate_validator",
    "citationsummary_validator",
    "claim_validator",
    "claimaccident_validator",
    "claimcareteam_validator",
    "claimdiagnosis_validator",
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
    "claimresponseadditemdetailsubdetail_validator",
    "claimresponseerror_validator",
    "claimresponseinsurance_validator",
    "claimresponseitem_validator",
    "claimresponseitemadjudication_validator",
    "claimresponseitemdetail_validator",
    "claimresponseitemdetailsubdetail_validator",
    "claimresponsepayment_validator",
    "claimresponseprocessnote_validator",
    "claimresponsetotal_validator",
    "claimsupportinginfo_validator",
    "clinicalimpression_validator",
    "clinicalimpressionfinding_validator",
    "clinicalimpressioninvestigation_validator",
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
    "consentpolicy_validator",
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
    "coverageeligibilityrequestinsurance_validator",
    "coverageeligibilityrequestitem_validator",
    "coverageeligibilityrequestitemdiagnosis_validator",
    "coverageeligibilityrequestsupportinginfo_validator",
    "coverageeligibilityresponse_validator",
    "coverageeligibilityresponseerror_validator",
    "coverageeligibilityresponseinsurance_validator",
    "coverageeligibilityresponseinsuranceitem_validator",
    "coverageeligibilityresponseinsuranceitembenefit_validator",
    "datarequirement_validator",
    "datarequirementcodefilter_validator",
    "datarequirementdatefilter_validator",
    "datarequirementsort_validator",
    "detectedissue_validator",
    "detectedissueevidence_validator",
    "detectedissuemitigation_validator",
    "device_validator",
    "devicedefinition_validator",
    "devicedefinitioncapability_validator",
    "devicedefinitiondevicename_validator",
    "devicedefinitionmaterial_validator",
    "devicedefinitionproperty_validator",
    "devicedefinitionspecialization_validator",
    "devicedefinitionudideviceidentifier_validator",
    "devicedevicename_validator",
    "devicemetric_validator",
    "devicemetriccalibration_validator",
    "deviceproperty_validator",
    "devicerequest_validator",
    "devicerequestparameter_validator",
    "devicespecialization_validator",
    "deviceudicarrier_validator",
    "deviceusestatement_validator",
    "deviceversion_validator",
    "diagnosticreport_validator",
    "diagnosticreportmedia_validator",
    "distance_validator",
    "documentmanifest_validator",
    "documentmanifestrelated_validator",
    "documentreference_validator",
    "documentreferencecontent_validator",
    "documentreferencecontext_validator",
    "documentreferencerelatesto_validator",
    "domainresource_validator",
    "dosage_validator",
    "dosagedoseandrate_validator",
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
    "eventdefinition_validator",
    "evidence_validator",
    "evidencecertainty_validator",
    "evidencereport_validator",
    "evidencereportrelatesto_validator",
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
    "evidencevariablecharacteristictimefromstart_validator",
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
    "explanationofbenefitadditemdetail_validator",
    "explanationofbenefitadditemdetailsubdetail_validator",
    "explanationofbenefitbenefitbalance_validator",
    "explanationofbenefitbenefitbalancefinancial_validator",
    "explanationofbenefitcareteam_validator",
    "explanationofbenefitdiagnosis_validator",
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
    "explanationofbenefitsupportinginfo_validator",
    "explanationofbenefittotal_validator",
    "expression_validator",
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
    "healthcareserviceeligibility_validator",
    "healthcareservicenotavailable_validator",
    "humanname_validator",
    "identifier_validator",
    "imagingstudy_validator",
    "imagingstudyseries_validator",
    "imagingstudyseriesinstance_validator",
    "imagingstudyseriesperformer_validator",
    "immunization_validator",
    "immunizationeducation_validator",
    "immunizationevaluation_validator",
    "immunizationperformer_validator",
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
    "insuranceplancontact_validator",
    "insuranceplancoverage_validator",
    "insuranceplancoveragebenefit_validator",
    "insuranceplancoveragebenefitlimit_validator",
    "insuranceplanplan_validator",
    "insuranceplanplangeneralcost_validator",
    "insuranceplanplanspecificcost_validator",
    "insuranceplanplanspecificcostbenefit_validator",
    "insuranceplanplanspecificcostbenefitcost_validator",
    "invoice_validator",
    "invoicelineitem_validator",
    "invoicelineitempricecomponent_validator",
    "invoiceparticipant_validator",
    "library_validator",
    "linkage_validator",
    "linkageitem_validator",
    "list_validator",
    "listentry_validator",
    "location_validator",
    "locationhoursofoperation_validator",
    "locationposition_validator",
    "manufactureditemdefinition_validator",
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
    "media_validator",
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
    "medicationknowledgeadministrationguidelines_validator",
    "medicationknowledgeadministrationguidelinesdosage_validator",
    "medicationknowledgeadministrationguidelinespatientcharacteristics_validator",
    "medicationknowledgecost_validator",
    "medicationknowledgedrugcharacteristic_validator",
    "medicationknowledgeingredient_validator",
    "medicationknowledgekinetics_validator",
    "medicationknowledgemedicineclassification_validator",
    "medicationknowledgemonitoringprogram_validator",
    "medicationknowledgemonograph_validator",
    "medicationknowledgepackaging_validator",
    "medicationknowledgeregulatory_validator",
    "medicationknowledgeregulatorymaxdispense_validator",
    "medicationknowledgeregulatoryschedule_validator",
    "medicationknowledgeregulatorysubstitution_validator",
    "medicationknowledgerelatedmedicationknowledge_validator",
    "medicationrequest_validator",
    "medicationrequestdispenserequest_validator",
    "medicationrequestdispenserequestinitialfill_validator",
    "medicationrequestsubstitution_validator",
    "medicationstatement_validator",
    "medicinalproductdefinition_validator",
    "medicinalproductdefinitioncharacteristic_validator",
    "medicinalproductdefinitioncontact_validator",
    "medicinalproductdefinitioncrossreference_validator",
    "medicinalproductdefinitionname_validator",
    "medicinalproductdefinitionnamecountrylanguage_validator",
    "medicinalproductdefinitionnamenamepart_validator",
    "medicinalproductdefinitionoperation_validator",
    "messagedefinition_validator",
    "messagedefinitionallowedresponse_validator",
    "messagedefinitionfocus_validator",
    "messageheader_validator",
    "messageheaderdestination_validator",
    "messageheaderresponse_validator",
    "messageheadersource_validator",
    "meta_validator",
    "molecularsequence_validator",
    "molecularsequencequality_validator",
    "molecularsequencequalityroc_validator",
    "molecularsequencereferenceseq_validator",
    "molecularsequencerepository_validator",
    "molecularsequencestructurevariant_validator",
    "molecularsequencestructurevariantinner_validator",
    "molecularsequencestructurevariantouter_validator",
    "molecularsequencevariant_validator",
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
    "nutritionproduct_validator",
    "nutritionproductingredient_validator",
    "nutritionproductinstance_validator",
    "nutritionproductnutrient_validator",
    "nutritionproductproductcharacteristic_validator",
    "observation_validator",
    "observationcomponent_validator",
    "observationdefinition_validator",
    "observationdefinitionqualifiedinterval_validator",
    "observationdefinitionquantitativedetails_validator",
    "observationreferencerange_validator",
    "operationdefinition_validator",
    "operationdefinitionoverload_validator",
    "operationdefinitionparameter_validator",
    "operationdefinitionparameterbinding_validator",
    "operationdefinitionparameterreferencedfrom_validator",
    "operationoutcome_validator",
    "operationoutcomeissue_validator",
    "organization_validator",
    "organizationaffiliation_validator",
    "organizationcontact_validator",
    "packagedproductdefinition_validator",
    "packagedproductdefinitionlegalstatusofsupply_validator",
    "packagedproductdefinitionpackage_validator",
    "packagedproductdefinitionpackagecontaineditem_validator",
    "packagedproductdefinitionpackageproperty_validator",
    "packagedproductdefinitionpackageshelflifestorage_validator",
    "parameterdefinition_validator",
    "parameters_validator",
    "parametersparameter_validator",
    "patient_validator",
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
    "population_validator",
    "practitioner_validator",
    "practitionerqualification_validator",
    "practitionerrole_validator",
    "practitionerroleavailabletime_validator",
    "practitionerrolenotavailable_validator",
    "procedure_validator",
    "procedurefocaldevice_validator",
    "procedureperformer_validator",
    "prodcharacteristic_validator",
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
    "requestgroup_validator",
    "requestgroupaction_validator",
    "requestgroupactioncondition_validator",
    "requestgroupactionrelatedaction_validator",
    "researchdefinition_validator",
    "researchelementdefinition_validator",
    "researchelementdefinitioncharacteristic_validator",
    "researchstudy_validator",
    "researchstudyarm_validator",
    "researchstudyobjective_validator",
    "researchsubject_validator",
    "resource_validator",
    "riskassessment_validator",
    "riskassessmentprediction_validator",
    "sampleddata_validator",
    "schedule_validator",
    "searchparameter_validator",
    "searchparametercomponent_validator",
    "servicerequest_validator",
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
    "specimenprocessing_validator",
    "structuredefinition_validator",
    "structuredefinitioncontext_validator",
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
    "substanceinstance_validator",
    "supplydelivery_validator",
    "supplydeliverysupplieditem_validator",
    "supplyrequest_validator",
    "supplyrequestparameter_validator",
    "task_validator",
    "taskinput_validator",
    "taskoutput_validator",
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
    "testscriptsetup_validator",
    "testscriptsetupaction_validator",
    "testscriptsetupactionassert_validator",
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
    "verificationresult_validator",
    "verificationresultattestation_validator",
    "verificationresultprimarysource_validator",
    "verificationresultvalidator_validator",
    "visionprescription_validator",
    "visionprescriptionlensspecification_validator",
    "visionprescriptionlensspecificationprism_validator",
]
