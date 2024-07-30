from __future__ import annotations as _annotations

from fhir_core.types import (
    Base64BinaryType,
    BooleanType,
    CanonicalType,
    CodeType,
    DateTimeType,
    DateType,
    DecimalType,
    IdType,
    InstantType,
    Integer64Type,
    IntegerType,
    MarkdownType,
    OidType,
    PositiveIntType,
    StringType,
    TimeType,
    UnsignedIntType,
    UriType,
    UrlType,
    UuidType,
    XhtmlType,
    create_fhir_element_or_resource_type,
    create_fhir_type,
)

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"


FHIRPrimitiveExtensionType = create_fhir_type(
    "FHIRPrimitiveExtensionType",
    "fhir.resources.STU3.fhirprimitiveextension.FHIRPrimitiveExtension",
)

ElementType = create_fhir_element_or_resource_type(
    "ElementType", "fhir.resources.STU3.element.Element"
)

ResourceType = create_fhir_element_or_resource_type(
    "ResourceType", "fhir.resources.STU3.resource.Resource"
)
AccountType = create_fhir_type("AccountType", "fhir.resources.STU3.account.Account")

AccountCoverageType = create_fhir_type(
    "AccountCoverageType", "fhir.resources.STU3.account.AccountCoverage"
)

AccountGuarantorType = create_fhir_type(
    "AccountGuarantorType", "fhir.resources.STU3.account.AccountGuarantor"
)

ActivityDefinitionType = create_fhir_type(
    "ActivityDefinitionType",
    "fhir.resources.STU3.activitydefinition.ActivityDefinition",
)

ActivityDefinitionDynamicValueType = create_fhir_type(
    "ActivityDefinitionDynamicValueType",
    "fhir.resources.STU3.activitydefinition.ActivityDefinitionDynamicValue",
)

ActivityDefinitionParticipantType = create_fhir_type(
    "ActivityDefinitionParticipantType",
    "fhir.resources.STU3.activitydefinition.ActivityDefinitionParticipant",
)

AddressType = create_fhir_type("AddressType", "fhir.resources.STU3.address.Address")

AdverseEventType = create_fhir_type(
    "AdverseEventType", "fhir.resources.STU3.adverseevent.AdverseEvent"
)

AdverseEventSuspectEntityType = create_fhir_type(
    "AdverseEventSuspectEntityType",
    "fhir.resources.STU3.adverseevent.AdverseEventSuspectEntity",
)

AgeType = create_fhir_type("AgeType", "fhir.resources.STU3.age.Age")

AllergyIntoleranceType = create_fhir_type(
    "AllergyIntoleranceType",
    "fhir.resources.STU3.allergyintolerance.AllergyIntolerance",
)

AllergyIntoleranceReactionType = create_fhir_type(
    "AllergyIntoleranceReactionType",
    "fhir.resources.STU3.allergyintolerance.AllergyIntoleranceReaction",
)

AnnotationType = create_fhir_type(
    "AnnotationType", "fhir.resources.STU3.annotation.Annotation"
)

AppointmentType = create_fhir_type(
    "AppointmentType", "fhir.resources.STU3.appointment.Appointment"
)

AppointmentParticipantType = create_fhir_type(
    "AppointmentParticipantType",
    "fhir.resources.STU3.appointment.AppointmentParticipant",
)

AppointmentResponseType = create_fhir_type(
    "AppointmentResponseType",
    "fhir.resources.STU3.appointmentresponse.AppointmentResponse",
)

AttachmentType = create_fhir_type(
    "AttachmentType", "fhir.resources.STU3.attachment.Attachment"
)

AuditEventType = create_fhir_type(
    "AuditEventType", "fhir.resources.STU3.auditevent.AuditEvent"
)

AuditEventAgentType = create_fhir_type(
    "AuditEventAgentType", "fhir.resources.STU3.auditevent.AuditEventAgent"
)

AuditEventAgentNetworkType = create_fhir_type(
    "AuditEventAgentNetworkType",
    "fhir.resources.STU3.auditevent.AuditEventAgentNetwork",
)

AuditEventEntityType = create_fhir_type(
    "AuditEventEntityType", "fhir.resources.STU3.auditevent.AuditEventEntity"
)

AuditEventEntityDetailType = create_fhir_type(
    "AuditEventEntityDetailType",
    "fhir.resources.STU3.auditevent.AuditEventEntityDetail",
)

AuditEventSourceType = create_fhir_type(
    "AuditEventSourceType", "fhir.resources.STU3.auditevent.AuditEventSource"
)

BackboneElementType = create_fhir_type(
    "BackboneElementType", "fhir.resources.STU3.backboneelement.BackboneElement"
)

BasicType = create_fhir_type("BasicType", "fhir.resources.STU3.basic.Basic")

BinaryType = create_fhir_type("BinaryType", "fhir.resources.STU3.binary.Binary")

BodySiteType = create_fhir_type("BodySiteType", "fhir.resources.STU3.bodysite.BodySite")

BundleType = create_fhir_type("BundleType", "fhir.resources.STU3.bundle.Bundle")

BundleEntryType = create_fhir_type(
    "BundleEntryType", "fhir.resources.STU3.bundle.BundleEntry"
)

BundleEntryRequestType = create_fhir_type(
    "BundleEntryRequestType", "fhir.resources.STU3.bundle.BundleEntryRequest"
)

BundleEntryResponseType = create_fhir_type(
    "BundleEntryResponseType", "fhir.resources.STU3.bundle.BundleEntryResponse"
)

BundleEntrySearchType = create_fhir_type(
    "BundleEntrySearchType", "fhir.resources.STU3.bundle.BundleEntrySearch"
)

BundleLinkType = create_fhir_type(
    "BundleLinkType", "fhir.resources.STU3.bundle.BundleLink"
)

CapabilityStatementType = create_fhir_type(
    "CapabilityStatementType",
    "fhir.resources.STU3.capabilitystatement.CapabilityStatement",
)

CapabilityStatementDocumentType = create_fhir_type(
    "CapabilityStatementDocumentType",
    "fhir.resources.STU3.capabilitystatement.CapabilityStatementDocument",
)

CapabilityStatementImplementationType = create_fhir_type(
    "CapabilityStatementImplementationType",
    "fhir.resources.STU3.capabilitystatement.CapabilityStatementImplementation",
)

CapabilityStatementMessagingType = create_fhir_type(
    "CapabilityStatementMessagingType",
    "fhir.resources.STU3.capabilitystatement.CapabilityStatementMessaging",
)

CapabilityStatementMessagingEndpointType = create_fhir_type(
    "CapabilityStatementMessagingEndpointType",
    "fhir.resources.STU3.capabilitystatement.CapabilityStatementMessagingEndpoint",
)

CapabilityStatementMessagingEventType = create_fhir_type(
    "CapabilityStatementMessagingEventType",
    "fhir.resources.STU3.capabilitystatement.CapabilityStatementMessagingEvent",
)

CapabilityStatementMessagingSupportedMessageType = create_fhir_type(
    "CapabilityStatementMessagingSupportedMessageType",
    "fhir.resources.STU3.capabilitystatement.CapabilityStatementMessagingSupportedMessage",
)

CapabilityStatementRestType = create_fhir_type(
    "CapabilityStatementRestType",
    "fhir.resources.STU3.capabilitystatement.CapabilityStatementRest",
)

CapabilityStatementRestInteractionType = create_fhir_type(
    "CapabilityStatementRestInteractionType",
    "fhir.resources.STU3.capabilitystatement.CapabilityStatementRestInteraction",
)

CapabilityStatementRestOperationType = create_fhir_type(
    "CapabilityStatementRestOperationType",
    "fhir.resources.STU3.capabilitystatement.CapabilityStatementRestOperation",
)

CapabilityStatementRestResourceType = create_fhir_type(
    "CapabilityStatementRestResourceType",
    "fhir.resources.STU3.capabilitystatement.CapabilityStatementRestResource",
)

CapabilityStatementRestResourceInteractionType = create_fhir_type(
    "CapabilityStatementRestResourceInteractionType",
    "fhir.resources.STU3.capabilitystatement.CapabilityStatementRestResourceInteraction",
)

CapabilityStatementRestResourceSearchParamType = create_fhir_type(
    "CapabilityStatementRestResourceSearchParamType",
    "fhir.resources.STU3.capabilitystatement.CapabilityStatementRestResourceSearchParam",
)

CapabilityStatementRestSecurityType = create_fhir_type(
    "CapabilityStatementRestSecurityType",
    "fhir.resources.STU3.capabilitystatement.CapabilityStatementRestSecurity",
)

CapabilityStatementRestSecurityCertificateType = create_fhir_type(
    "CapabilityStatementRestSecurityCertificateType",
    "fhir.resources.STU3.capabilitystatement.CapabilityStatementRestSecurityCertificate",
)

CapabilityStatementSoftwareType = create_fhir_type(
    "CapabilityStatementSoftwareType",
    "fhir.resources.STU3.capabilitystatement.CapabilityStatementSoftware",
)

CarePlanType = create_fhir_type("CarePlanType", "fhir.resources.STU3.careplan.CarePlan")

CarePlanActivityType = create_fhir_type(
    "CarePlanActivityType", "fhir.resources.STU3.careplan.CarePlanActivity"
)

CarePlanActivityDetailType = create_fhir_type(
    "CarePlanActivityDetailType", "fhir.resources.STU3.careplan.CarePlanActivityDetail"
)

CareTeamType = create_fhir_type("CareTeamType", "fhir.resources.STU3.careteam.CareTeam")

CareTeamParticipantType = create_fhir_type(
    "CareTeamParticipantType", "fhir.resources.STU3.careteam.CareTeamParticipant"
)

ChargeItemType = create_fhir_type(
    "ChargeItemType", "fhir.resources.STU3.chargeitem.ChargeItem"
)

ChargeItemParticipantType = create_fhir_type(
    "ChargeItemParticipantType", "fhir.resources.STU3.chargeitem.ChargeItemParticipant"
)

ClaimType = create_fhir_type("ClaimType", "fhir.resources.STU3.claim.Claim")

ClaimAccidentType = create_fhir_type(
    "ClaimAccidentType", "fhir.resources.STU3.claim.ClaimAccident"
)

ClaimCareTeamType = create_fhir_type(
    "ClaimCareTeamType", "fhir.resources.STU3.claim.ClaimCareTeam"
)

ClaimDiagnosisType = create_fhir_type(
    "ClaimDiagnosisType", "fhir.resources.STU3.claim.ClaimDiagnosis"
)

ClaimInformationType = create_fhir_type(
    "ClaimInformationType", "fhir.resources.STU3.claim.ClaimInformation"
)

ClaimInsuranceType = create_fhir_type(
    "ClaimInsuranceType", "fhir.resources.STU3.claim.ClaimInsurance"
)

ClaimItemType = create_fhir_type("ClaimItemType", "fhir.resources.STU3.claim.ClaimItem")

ClaimItemDetailType = create_fhir_type(
    "ClaimItemDetailType", "fhir.resources.STU3.claim.ClaimItemDetail"
)

ClaimItemDetailSubDetailType = create_fhir_type(
    "ClaimItemDetailSubDetailType", "fhir.resources.STU3.claim.ClaimItemDetailSubDetail"
)

ClaimPayeeType = create_fhir_type(
    "ClaimPayeeType", "fhir.resources.STU3.claim.ClaimPayee"
)

ClaimProcedureType = create_fhir_type(
    "ClaimProcedureType", "fhir.resources.STU3.claim.ClaimProcedure"
)

ClaimRelatedType = create_fhir_type(
    "ClaimRelatedType", "fhir.resources.STU3.claim.ClaimRelated"
)

ClaimResponseType = create_fhir_type(
    "ClaimResponseType", "fhir.resources.STU3.claimresponse.ClaimResponse"
)

ClaimResponseAddItemType = create_fhir_type(
    "ClaimResponseAddItemType", "fhir.resources.STU3.claimresponse.ClaimResponseAddItem"
)

ClaimResponseAddItemDetailType = create_fhir_type(
    "ClaimResponseAddItemDetailType",
    "fhir.resources.STU3.claimresponse.ClaimResponseAddItemDetail",
)

ClaimResponseErrorType = create_fhir_type(
    "ClaimResponseErrorType", "fhir.resources.STU3.claimresponse.ClaimResponseError"
)

ClaimResponseInsuranceType = create_fhir_type(
    "ClaimResponseInsuranceType",
    "fhir.resources.STU3.claimresponse.ClaimResponseInsurance",
)

ClaimResponseItemType = create_fhir_type(
    "ClaimResponseItemType", "fhir.resources.STU3.claimresponse.ClaimResponseItem"
)

ClaimResponseItemAdjudicationType = create_fhir_type(
    "ClaimResponseItemAdjudicationType",
    "fhir.resources.STU3.claimresponse.ClaimResponseItemAdjudication",
)

ClaimResponseItemDetailType = create_fhir_type(
    "ClaimResponseItemDetailType",
    "fhir.resources.STU3.claimresponse.ClaimResponseItemDetail",
)

ClaimResponseItemDetailSubDetailType = create_fhir_type(
    "ClaimResponseItemDetailSubDetailType",
    "fhir.resources.STU3.claimresponse.ClaimResponseItemDetailSubDetail",
)

ClaimResponsePaymentType = create_fhir_type(
    "ClaimResponsePaymentType", "fhir.resources.STU3.claimresponse.ClaimResponsePayment"
)

ClaimResponseProcessNoteType = create_fhir_type(
    "ClaimResponseProcessNoteType",
    "fhir.resources.STU3.claimresponse.ClaimResponseProcessNote",
)

ClinicalImpressionType = create_fhir_type(
    "ClinicalImpressionType",
    "fhir.resources.STU3.clinicalimpression.ClinicalImpression",
)

ClinicalImpressionFindingType = create_fhir_type(
    "ClinicalImpressionFindingType",
    "fhir.resources.STU3.clinicalimpression.ClinicalImpressionFinding",
)

ClinicalImpressionInvestigationType = create_fhir_type(
    "ClinicalImpressionInvestigationType",
    "fhir.resources.STU3.clinicalimpression.ClinicalImpressionInvestigation",
)

CodeSystemType = create_fhir_type(
    "CodeSystemType", "fhir.resources.STU3.codesystem.CodeSystem"
)

CodeSystemConceptType = create_fhir_type(
    "CodeSystemConceptType", "fhir.resources.STU3.codesystem.CodeSystemConcept"
)

CodeSystemConceptDesignationType = create_fhir_type(
    "CodeSystemConceptDesignationType",
    "fhir.resources.STU3.codesystem.CodeSystemConceptDesignation",
)

CodeSystemConceptPropertyType = create_fhir_type(
    "CodeSystemConceptPropertyType",
    "fhir.resources.STU3.codesystem.CodeSystemConceptProperty",
)

CodeSystemFilterType = create_fhir_type(
    "CodeSystemFilterType", "fhir.resources.STU3.codesystem.CodeSystemFilter"
)

CodeSystemPropertyType = create_fhir_type(
    "CodeSystemPropertyType", "fhir.resources.STU3.codesystem.CodeSystemProperty"
)

CodeableConceptType = create_fhir_type(
    "CodeableConceptType", "fhir.resources.STU3.codeableconcept.CodeableConcept"
)

CodingType = create_fhir_type("CodingType", "fhir.resources.STU3.coding.Coding")

CommunicationType = create_fhir_type(
    "CommunicationType", "fhir.resources.STU3.communication.Communication"
)

CommunicationPayloadType = create_fhir_type(
    "CommunicationPayloadType", "fhir.resources.STU3.communication.CommunicationPayload"
)

CommunicationRequestType = create_fhir_type(
    "CommunicationRequestType",
    "fhir.resources.STU3.communicationrequest.CommunicationRequest",
)

CommunicationRequestPayloadType = create_fhir_type(
    "CommunicationRequestPayloadType",
    "fhir.resources.STU3.communicationrequest.CommunicationRequestPayload",
)

CommunicationRequestRequesterType = create_fhir_type(
    "CommunicationRequestRequesterType",
    "fhir.resources.STU3.communicationrequest.CommunicationRequestRequester",
)

CompartmentDefinitionType = create_fhir_type(
    "CompartmentDefinitionType",
    "fhir.resources.STU3.compartmentdefinition.CompartmentDefinition",
)

CompartmentDefinitionResourceType = create_fhir_type(
    "CompartmentDefinitionResourceType",
    "fhir.resources.STU3.compartmentdefinition.CompartmentDefinitionResource",
)

CompositionType = create_fhir_type(
    "CompositionType", "fhir.resources.STU3.composition.Composition"
)

CompositionAttesterType = create_fhir_type(
    "CompositionAttesterType", "fhir.resources.STU3.composition.CompositionAttester"
)

CompositionEventType = create_fhir_type(
    "CompositionEventType", "fhir.resources.STU3.composition.CompositionEvent"
)

CompositionRelatesToType = create_fhir_type(
    "CompositionRelatesToType", "fhir.resources.STU3.composition.CompositionRelatesTo"
)

CompositionSectionType = create_fhir_type(
    "CompositionSectionType", "fhir.resources.STU3.composition.CompositionSection"
)

ConceptMapType = create_fhir_type(
    "ConceptMapType", "fhir.resources.STU3.conceptmap.ConceptMap"
)

ConceptMapGroupType = create_fhir_type(
    "ConceptMapGroupType", "fhir.resources.STU3.conceptmap.ConceptMapGroup"
)

ConceptMapGroupElementType = create_fhir_type(
    "ConceptMapGroupElementType",
    "fhir.resources.STU3.conceptmap.ConceptMapGroupElement",
)

ConceptMapGroupElementTargetType = create_fhir_type(
    "ConceptMapGroupElementTargetType",
    "fhir.resources.STU3.conceptmap.ConceptMapGroupElementTarget",
)

ConceptMapGroupElementTargetDependsOnType = create_fhir_type(
    "ConceptMapGroupElementTargetDependsOnType",
    "fhir.resources.STU3.conceptmap.ConceptMapGroupElementTargetDependsOn",
)

ConceptMapGroupUnmappedType = create_fhir_type(
    "ConceptMapGroupUnmappedType",
    "fhir.resources.STU3.conceptmap.ConceptMapGroupUnmapped",
)

ConditionType = create_fhir_type(
    "ConditionType", "fhir.resources.STU3.condition.Condition"
)

ConditionEvidenceType = create_fhir_type(
    "ConditionEvidenceType", "fhir.resources.STU3.condition.ConditionEvidence"
)

ConditionStageType = create_fhir_type(
    "ConditionStageType", "fhir.resources.STU3.condition.ConditionStage"
)

ConsentType = create_fhir_type("ConsentType", "fhir.resources.STU3.consent.Consent")

ConsentActorType = create_fhir_type(
    "ConsentActorType", "fhir.resources.STU3.consent.ConsentActor"
)

ConsentDataType = create_fhir_type(
    "ConsentDataType", "fhir.resources.STU3.consent.ConsentData"
)

ConsentExceptType = create_fhir_type(
    "ConsentExceptType", "fhir.resources.STU3.consent.ConsentExcept"
)

ConsentExceptActorType = create_fhir_type(
    "ConsentExceptActorType", "fhir.resources.STU3.consent.ConsentExceptActor"
)

ConsentExceptDataType = create_fhir_type(
    "ConsentExceptDataType", "fhir.resources.STU3.consent.ConsentExceptData"
)

ConsentPolicyType = create_fhir_type(
    "ConsentPolicyType", "fhir.resources.STU3.consent.ConsentPolicy"
)

ContactDetailType = create_fhir_type(
    "ContactDetailType", "fhir.resources.STU3.contactdetail.ContactDetail"
)

ContactPointType = create_fhir_type(
    "ContactPointType", "fhir.resources.STU3.contactpoint.ContactPoint"
)

ContractType = create_fhir_type("ContractType", "fhir.resources.STU3.contract.Contract")

ContractAgentType = create_fhir_type(
    "ContractAgentType", "fhir.resources.STU3.contract.ContractAgent"
)

ContractFriendlyType = create_fhir_type(
    "ContractFriendlyType", "fhir.resources.STU3.contract.ContractFriendly"
)

ContractLegalType = create_fhir_type(
    "ContractLegalType", "fhir.resources.STU3.contract.ContractLegal"
)

ContractRuleType = create_fhir_type(
    "ContractRuleType", "fhir.resources.STU3.contract.ContractRule"
)

ContractSignerType = create_fhir_type(
    "ContractSignerType", "fhir.resources.STU3.contract.ContractSigner"
)

ContractTermType = create_fhir_type(
    "ContractTermType", "fhir.resources.STU3.contract.ContractTerm"
)

ContractTermAgentType = create_fhir_type(
    "ContractTermAgentType", "fhir.resources.STU3.contract.ContractTermAgent"
)

ContractTermValuedItemType = create_fhir_type(
    "ContractTermValuedItemType", "fhir.resources.STU3.contract.ContractTermValuedItem"
)

ContractValuedItemType = create_fhir_type(
    "ContractValuedItemType", "fhir.resources.STU3.contract.ContractValuedItem"
)

ContributorType = create_fhir_type(
    "ContributorType", "fhir.resources.STU3.contributor.Contributor"
)

CountType = create_fhir_type("CountType", "fhir.resources.STU3.count.Count")

CoverageType = create_fhir_type("CoverageType", "fhir.resources.STU3.coverage.Coverage")

CoverageGroupingType = create_fhir_type(
    "CoverageGroupingType", "fhir.resources.STU3.coverage.CoverageGrouping"
)

DataElementType = create_fhir_type(
    "DataElementType", "fhir.resources.STU3.dataelement.DataElement"
)

DataElementMappingType = create_fhir_type(
    "DataElementMappingType", "fhir.resources.STU3.dataelement.DataElementMapping"
)

DataRequirementType = create_fhir_type(
    "DataRequirementType", "fhir.resources.STU3.datarequirement.DataRequirement"
)

DataRequirementCodeFilterType = create_fhir_type(
    "DataRequirementCodeFilterType",
    "fhir.resources.STU3.datarequirement.DataRequirementCodeFilter",
)

DataRequirementDateFilterType = create_fhir_type(
    "DataRequirementDateFilterType",
    "fhir.resources.STU3.datarequirement.DataRequirementDateFilter",
)

DetectedIssueType = create_fhir_type(
    "DetectedIssueType", "fhir.resources.STU3.detectedissue.DetectedIssue"
)

DetectedIssueMitigationType = create_fhir_type(
    "DetectedIssueMitigationType",
    "fhir.resources.STU3.detectedissue.DetectedIssueMitigation",
)

DeviceType = create_fhir_type("DeviceType", "fhir.resources.STU3.device.Device")

DeviceComponentType = create_fhir_type(
    "DeviceComponentType", "fhir.resources.STU3.devicecomponent.DeviceComponent"
)

DeviceComponentProductionSpecificationType = create_fhir_type(
    "DeviceComponentProductionSpecificationType",
    "fhir.resources.STU3.devicecomponent.DeviceComponentProductionSpecification",
)

DeviceMetricType = create_fhir_type(
    "DeviceMetricType", "fhir.resources.STU3.devicemetric.DeviceMetric"
)

DeviceMetricCalibrationType = create_fhir_type(
    "DeviceMetricCalibrationType",
    "fhir.resources.STU3.devicemetric.DeviceMetricCalibration",
)

DeviceRequestType = create_fhir_type(
    "DeviceRequestType", "fhir.resources.STU3.devicerequest.DeviceRequest"
)

DeviceRequestRequesterType = create_fhir_type(
    "DeviceRequestRequesterType",
    "fhir.resources.STU3.devicerequest.DeviceRequestRequester",
)

DeviceUdiType = create_fhir_type(
    "DeviceUdiType", "fhir.resources.STU3.device.DeviceUdi"
)

DeviceUseStatementType = create_fhir_type(
    "DeviceUseStatementType",
    "fhir.resources.STU3.deviceusestatement.DeviceUseStatement",
)

DiagnosticReportType = create_fhir_type(
    "DiagnosticReportType", "fhir.resources.STU3.diagnosticreport.DiagnosticReport"
)

DiagnosticReportImageType = create_fhir_type(
    "DiagnosticReportImageType",
    "fhir.resources.STU3.diagnosticreport.DiagnosticReportImage",
)

DiagnosticReportPerformerType = create_fhir_type(
    "DiagnosticReportPerformerType",
    "fhir.resources.STU3.diagnosticreport.DiagnosticReportPerformer",
)

DistanceType = create_fhir_type("DistanceType", "fhir.resources.STU3.distance.Distance")

DocumentManifestType = create_fhir_type(
    "DocumentManifestType", "fhir.resources.STU3.documentmanifest.DocumentManifest"
)

DocumentManifestContentType = create_fhir_type(
    "DocumentManifestContentType",
    "fhir.resources.STU3.documentmanifest.DocumentManifestContent",
)

DocumentManifestRelatedType = create_fhir_type(
    "DocumentManifestRelatedType",
    "fhir.resources.STU3.documentmanifest.DocumentManifestRelated",
)

DocumentReferenceType = create_fhir_type(
    "DocumentReferenceType", "fhir.resources.STU3.documentreference.DocumentReference"
)

DocumentReferenceContentType = create_fhir_type(
    "DocumentReferenceContentType",
    "fhir.resources.STU3.documentreference.DocumentReferenceContent",
)

DocumentReferenceContextType = create_fhir_type(
    "DocumentReferenceContextType",
    "fhir.resources.STU3.documentreference.DocumentReferenceContext",
)

DocumentReferenceContextRelatedType = create_fhir_type(
    "DocumentReferenceContextRelatedType",
    "fhir.resources.STU3.documentreference.DocumentReferenceContextRelated",
)

DocumentReferenceRelatesToType = create_fhir_type(
    "DocumentReferenceRelatesToType",
    "fhir.resources.STU3.documentreference.DocumentReferenceRelatesTo",
)

DomainResourceType = create_fhir_type(
    "DomainResourceType", "fhir.resources.STU3.domainresource.DomainResource"
)

DosageType = create_fhir_type("DosageType", "fhir.resources.STU3.dosage.Dosage")

DurationType = create_fhir_type("DurationType", "fhir.resources.STU3.duration.Duration")

ElementDefinitionType = create_fhir_type(
    "ElementDefinitionType", "fhir.resources.STU3.elementdefinition.ElementDefinition"
)

ElementDefinitionBaseType = create_fhir_type(
    "ElementDefinitionBaseType",
    "fhir.resources.STU3.elementdefinition.ElementDefinitionBase",
)

ElementDefinitionBindingType = create_fhir_type(
    "ElementDefinitionBindingType",
    "fhir.resources.STU3.elementdefinition.ElementDefinitionBinding",
)

ElementDefinitionConstraintType = create_fhir_type(
    "ElementDefinitionConstraintType",
    "fhir.resources.STU3.elementdefinition.ElementDefinitionConstraint",
)

ElementDefinitionExampleType = create_fhir_type(
    "ElementDefinitionExampleType",
    "fhir.resources.STU3.elementdefinition.ElementDefinitionExample",
)

ElementDefinitionMappingType = create_fhir_type(
    "ElementDefinitionMappingType",
    "fhir.resources.STU3.elementdefinition.ElementDefinitionMapping",
)

ElementDefinitionSlicingType = create_fhir_type(
    "ElementDefinitionSlicingType",
    "fhir.resources.STU3.elementdefinition.ElementDefinitionSlicing",
)

ElementDefinitionSlicingDiscriminatorType = create_fhir_type(
    "ElementDefinitionSlicingDiscriminatorType",
    "fhir.resources.STU3.elementdefinition.ElementDefinitionSlicingDiscriminator",
)

ElementDefinitionTypeType = create_fhir_type(
    "ElementDefinitionTypeType",
    "fhir.resources.STU3.elementdefinition.ElementDefinitionType",
)

EligibilityRequestType = create_fhir_type(
    "EligibilityRequestType",
    "fhir.resources.STU3.eligibilityrequest.EligibilityRequest",
)

EligibilityResponseType = create_fhir_type(
    "EligibilityResponseType",
    "fhir.resources.STU3.eligibilityresponse.EligibilityResponse",
)

EligibilityResponseErrorType = create_fhir_type(
    "EligibilityResponseErrorType",
    "fhir.resources.STU3.eligibilityresponse.EligibilityResponseError",
)

EligibilityResponseInsuranceType = create_fhir_type(
    "EligibilityResponseInsuranceType",
    "fhir.resources.STU3.eligibilityresponse.EligibilityResponseInsurance",
)

EligibilityResponseInsuranceBenefitBalanceType = create_fhir_type(
    "EligibilityResponseInsuranceBenefitBalanceType",
    "fhir.resources.STU3.eligibilityresponse.EligibilityResponseInsuranceBenefitBalance",
)

EligibilityResponseInsuranceBenefitBalanceFinancialType = create_fhir_type(
    "EligibilityResponseInsuranceBenefitBalanceFinancialType",
    "fhir.resources.STU3.eligibilityresponse.EligibilityResponseInsuranceBenefitBalanceFinancial",
)

EncounterType = create_fhir_type(
    "EncounterType", "fhir.resources.STU3.encounter.Encounter"
)

EncounterClassHistoryType = create_fhir_type(
    "EncounterClassHistoryType", "fhir.resources.STU3.encounter.EncounterClassHistory"
)

EncounterDiagnosisType = create_fhir_type(
    "EncounterDiagnosisType", "fhir.resources.STU3.encounter.EncounterDiagnosis"
)

EncounterHospitalizationType = create_fhir_type(
    "EncounterHospitalizationType",
    "fhir.resources.STU3.encounter.EncounterHospitalization",
)

EncounterLocationType = create_fhir_type(
    "EncounterLocationType", "fhir.resources.STU3.encounter.EncounterLocation"
)

EncounterParticipantType = create_fhir_type(
    "EncounterParticipantType", "fhir.resources.STU3.encounter.EncounterParticipant"
)

EncounterStatusHistoryType = create_fhir_type(
    "EncounterStatusHistoryType", "fhir.resources.STU3.encounter.EncounterStatusHistory"
)

EndpointType = create_fhir_type("EndpointType", "fhir.resources.STU3.endpoint.Endpoint")

EnrollmentRequestType = create_fhir_type(
    "EnrollmentRequestType", "fhir.resources.STU3.enrollmentrequest.EnrollmentRequest"
)

EnrollmentResponseType = create_fhir_type(
    "EnrollmentResponseType",
    "fhir.resources.STU3.enrollmentresponse.EnrollmentResponse",
)

EpisodeOfCareType = create_fhir_type(
    "EpisodeOfCareType", "fhir.resources.STU3.episodeofcare.EpisodeOfCare"
)

EpisodeOfCareDiagnosisType = create_fhir_type(
    "EpisodeOfCareDiagnosisType",
    "fhir.resources.STU3.episodeofcare.EpisodeOfCareDiagnosis",
)

EpisodeOfCareStatusHistoryType = create_fhir_type(
    "EpisodeOfCareStatusHistoryType",
    "fhir.resources.STU3.episodeofcare.EpisodeOfCareStatusHistory",
)

ExpansionProfileType = create_fhir_type(
    "ExpansionProfileType", "fhir.resources.STU3.expansionprofile.ExpansionProfile"
)

ExpansionProfileDesignationType = create_fhir_type(
    "ExpansionProfileDesignationType",
    "fhir.resources.STU3.expansionprofile.ExpansionProfileDesignation",
)

ExpansionProfileDesignationExcludeType = create_fhir_type(
    "ExpansionProfileDesignationExcludeType",
    "fhir.resources.STU3.expansionprofile.ExpansionProfileDesignationExclude",
)

ExpansionProfileDesignationExcludeDesignationType = create_fhir_type(
    "ExpansionProfileDesignationExcludeDesignationType",
    "fhir.resources.STU3.expansionprofile.ExpansionProfileDesignationExcludeDesignation",
)

ExpansionProfileDesignationIncludeType = create_fhir_type(
    "ExpansionProfileDesignationIncludeType",
    "fhir.resources.STU3.expansionprofile.ExpansionProfileDesignationInclude",
)

ExpansionProfileDesignationIncludeDesignationType = create_fhir_type(
    "ExpansionProfileDesignationIncludeDesignationType",
    "fhir.resources.STU3.expansionprofile.ExpansionProfileDesignationIncludeDesignation",
)

ExpansionProfileExcludedSystemType = create_fhir_type(
    "ExpansionProfileExcludedSystemType",
    "fhir.resources.STU3.expansionprofile.ExpansionProfileExcludedSystem",
)

ExpansionProfileFixedVersionType = create_fhir_type(
    "ExpansionProfileFixedVersionType",
    "fhir.resources.STU3.expansionprofile.ExpansionProfileFixedVersion",
)

ExplanationOfBenefitType = create_fhir_type(
    "ExplanationOfBenefitType",
    "fhir.resources.STU3.explanationofbenefit.ExplanationOfBenefit",
)

ExplanationOfBenefitAccidentType = create_fhir_type(
    "ExplanationOfBenefitAccidentType",
    "fhir.resources.STU3.explanationofbenefit.ExplanationOfBenefitAccident",
)

ExplanationOfBenefitAddItemType = create_fhir_type(
    "ExplanationOfBenefitAddItemType",
    "fhir.resources.STU3.explanationofbenefit.ExplanationOfBenefitAddItem",
)

ExplanationOfBenefitAddItemDetailType = create_fhir_type(
    "ExplanationOfBenefitAddItemDetailType",
    "fhir.resources.STU3.explanationofbenefit.ExplanationOfBenefitAddItemDetail",
)

ExplanationOfBenefitBenefitBalanceType = create_fhir_type(
    "ExplanationOfBenefitBenefitBalanceType",
    "fhir.resources.STU3.explanationofbenefit.ExplanationOfBenefitBenefitBalance",
)

ExplanationOfBenefitBenefitBalanceFinancialType = create_fhir_type(
    "ExplanationOfBenefitBenefitBalanceFinancialType",
    "fhir.resources.STU3.explanationofbenefit.ExplanationOfBenefitBenefitBalanceFinancial",
)

ExplanationOfBenefitCareTeamType = create_fhir_type(
    "ExplanationOfBenefitCareTeamType",
    "fhir.resources.STU3.explanationofbenefit.ExplanationOfBenefitCareTeam",
)

ExplanationOfBenefitDiagnosisType = create_fhir_type(
    "ExplanationOfBenefitDiagnosisType",
    "fhir.resources.STU3.explanationofbenefit.ExplanationOfBenefitDiagnosis",
)

ExplanationOfBenefitInformationType = create_fhir_type(
    "ExplanationOfBenefitInformationType",
    "fhir.resources.STU3.explanationofbenefit.ExplanationOfBenefitInformation",
)

ExplanationOfBenefitInsuranceType = create_fhir_type(
    "ExplanationOfBenefitInsuranceType",
    "fhir.resources.STU3.explanationofbenefit.ExplanationOfBenefitInsurance",
)

ExplanationOfBenefitItemType = create_fhir_type(
    "ExplanationOfBenefitItemType",
    "fhir.resources.STU3.explanationofbenefit.ExplanationOfBenefitItem",
)

ExplanationOfBenefitItemAdjudicationType = create_fhir_type(
    "ExplanationOfBenefitItemAdjudicationType",
    "fhir.resources.STU3.explanationofbenefit.ExplanationOfBenefitItemAdjudication",
)

ExplanationOfBenefitItemDetailType = create_fhir_type(
    "ExplanationOfBenefitItemDetailType",
    "fhir.resources.STU3.explanationofbenefit.ExplanationOfBenefitItemDetail",
)

ExplanationOfBenefitItemDetailSubDetailType = create_fhir_type(
    "ExplanationOfBenefitItemDetailSubDetailType",
    "fhir.resources.STU3.explanationofbenefit.ExplanationOfBenefitItemDetailSubDetail",
)

ExplanationOfBenefitPayeeType = create_fhir_type(
    "ExplanationOfBenefitPayeeType",
    "fhir.resources.STU3.explanationofbenefit.ExplanationOfBenefitPayee",
)

ExplanationOfBenefitPaymentType = create_fhir_type(
    "ExplanationOfBenefitPaymentType",
    "fhir.resources.STU3.explanationofbenefit.ExplanationOfBenefitPayment",
)

ExplanationOfBenefitProcedureType = create_fhir_type(
    "ExplanationOfBenefitProcedureType",
    "fhir.resources.STU3.explanationofbenefit.ExplanationOfBenefitProcedure",
)

ExplanationOfBenefitProcessNoteType = create_fhir_type(
    "ExplanationOfBenefitProcessNoteType",
    "fhir.resources.STU3.explanationofbenefit.ExplanationOfBenefitProcessNote",
)

ExplanationOfBenefitRelatedType = create_fhir_type(
    "ExplanationOfBenefitRelatedType",
    "fhir.resources.STU3.explanationofbenefit.ExplanationOfBenefitRelated",
)

ExtensionType = create_fhir_type(
    "ExtensionType", "fhir.resources.STU3.extension.Extension"
)

FamilyMemberHistoryType = create_fhir_type(
    "FamilyMemberHistoryType",
    "fhir.resources.STU3.familymemberhistory.FamilyMemberHistory",
)

FamilyMemberHistoryConditionType = create_fhir_type(
    "FamilyMemberHistoryConditionType",
    "fhir.resources.STU3.familymemberhistory.FamilyMemberHistoryCondition",
)

FlagType = create_fhir_type("FlagType", "fhir.resources.STU3.flag.Flag")

GoalType = create_fhir_type("GoalType", "fhir.resources.STU3.goal.Goal")

GoalTargetType = create_fhir_type(
    "GoalTargetType", "fhir.resources.STU3.goal.GoalTarget"
)

GraphDefinitionType = create_fhir_type(
    "GraphDefinitionType", "fhir.resources.STU3.graphdefinition.GraphDefinition"
)

GraphDefinitionLinkType = create_fhir_type(
    "GraphDefinitionLinkType", "fhir.resources.STU3.graphdefinition.GraphDefinitionLink"
)

GraphDefinitionLinkTargetType = create_fhir_type(
    "GraphDefinitionLinkTargetType",
    "fhir.resources.STU3.graphdefinition.GraphDefinitionLinkTarget",
)

GraphDefinitionLinkTargetCompartmentType = create_fhir_type(
    "GraphDefinitionLinkTargetCompartmentType",
    "fhir.resources.STU3.graphdefinition.GraphDefinitionLinkTargetCompartment",
)

GroupType = create_fhir_type("GroupType", "fhir.resources.STU3.group.Group")

GroupCharacteristicType = create_fhir_type(
    "GroupCharacteristicType", "fhir.resources.STU3.group.GroupCharacteristic"
)

GroupMemberType = create_fhir_type(
    "GroupMemberType", "fhir.resources.STU3.group.GroupMember"
)

GuidanceResponseType = create_fhir_type(
    "GuidanceResponseType", "fhir.resources.STU3.guidanceresponse.GuidanceResponse"
)

HealthcareServiceType = create_fhir_type(
    "HealthcareServiceType", "fhir.resources.STU3.healthcareservice.HealthcareService"
)

HealthcareServiceAvailableTimeType = create_fhir_type(
    "HealthcareServiceAvailableTimeType",
    "fhir.resources.STU3.healthcareservice.HealthcareServiceAvailableTime",
)

HealthcareServiceNotAvailableType = create_fhir_type(
    "HealthcareServiceNotAvailableType",
    "fhir.resources.STU3.healthcareservice.HealthcareServiceNotAvailable",
)

HumanNameType = create_fhir_type(
    "HumanNameType", "fhir.resources.STU3.humanname.HumanName"
)

IdentifierType = create_fhir_type(
    "IdentifierType", "fhir.resources.STU3.identifier.Identifier"
)

ImagingManifestType = create_fhir_type(
    "ImagingManifestType", "fhir.resources.STU3.imagingmanifest.ImagingManifest"
)

ImagingManifestStudyType = create_fhir_type(
    "ImagingManifestStudyType",
    "fhir.resources.STU3.imagingmanifest.ImagingManifestStudy",
)

ImagingManifestStudySeriesType = create_fhir_type(
    "ImagingManifestStudySeriesType",
    "fhir.resources.STU3.imagingmanifest.ImagingManifestStudySeries",
)

ImagingManifestStudySeriesInstanceType = create_fhir_type(
    "ImagingManifestStudySeriesInstanceType",
    "fhir.resources.STU3.imagingmanifest.ImagingManifestStudySeriesInstance",
)

ImagingStudyType = create_fhir_type(
    "ImagingStudyType", "fhir.resources.STU3.imagingstudy.ImagingStudy"
)

ImagingStudySeriesType = create_fhir_type(
    "ImagingStudySeriesType", "fhir.resources.STU3.imagingstudy.ImagingStudySeries"
)

ImagingStudySeriesInstanceType = create_fhir_type(
    "ImagingStudySeriesInstanceType",
    "fhir.resources.STU3.imagingstudy.ImagingStudySeriesInstance",
)

ImmunizationType = create_fhir_type(
    "ImmunizationType", "fhir.resources.STU3.immunization.Immunization"
)

ImmunizationExplanationType = create_fhir_type(
    "ImmunizationExplanationType",
    "fhir.resources.STU3.immunization.ImmunizationExplanation",
)

ImmunizationPractitionerType = create_fhir_type(
    "ImmunizationPractitionerType",
    "fhir.resources.STU3.immunization.ImmunizationPractitioner",
)

ImmunizationReactionType = create_fhir_type(
    "ImmunizationReactionType", "fhir.resources.STU3.immunization.ImmunizationReaction"
)

ImmunizationRecommendationType = create_fhir_type(
    "ImmunizationRecommendationType",
    "fhir.resources.STU3.immunizationrecommendation.ImmunizationRecommendation",
)

ImmunizationRecommendationRecommendationType = create_fhir_type(
    "ImmunizationRecommendationRecommendationType",
    "fhir.resources.STU3.immunizationrecommendation.ImmunizationRecommendationRecommendation",
)

ImmunizationRecommendationRecommendationDateCriterionType = create_fhir_type(
    "ImmunizationRecommendationRecommendationDateCriterionType",
    "fhir.resources.STU3.immunizationrecommendation.ImmunizationRecommendationRecommendationDateCriterion",
)

ImmunizationRecommendationRecommendationProtocolType = create_fhir_type(
    "ImmunizationRecommendationRecommendationProtocolType",
    "fhir.resources.STU3.immunizationrecommendation.ImmunizationRecommendationRecommendationProtocol",
)

ImmunizationVaccinationProtocolType = create_fhir_type(
    "ImmunizationVaccinationProtocolType",
    "fhir.resources.STU3.immunization.ImmunizationVaccinationProtocol",
)

ImplementationGuideType = create_fhir_type(
    "ImplementationGuideType",
    "fhir.resources.STU3.implementationguide.ImplementationGuide",
)

ImplementationGuideDependencyType = create_fhir_type(
    "ImplementationGuideDependencyType",
    "fhir.resources.STU3.implementationguide.ImplementationGuideDependency",
)

ImplementationGuideGlobalType = create_fhir_type(
    "ImplementationGuideGlobalType",
    "fhir.resources.STU3.implementationguide.ImplementationGuideGlobal",
)

ImplementationGuidePackageType = create_fhir_type(
    "ImplementationGuidePackageType",
    "fhir.resources.STU3.implementationguide.ImplementationGuidePackage",
)

ImplementationGuidePackageResourceType = create_fhir_type(
    "ImplementationGuidePackageResourceType",
    "fhir.resources.STU3.implementationguide.ImplementationGuidePackageResource",
)

ImplementationGuidePageType = create_fhir_type(
    "ImplementationGuidePageType",
    "fhir.resources.STU3.implementationguide.ImplementationGuidePage",
)

LibraryType = create_fhir_type("LibraryType", "fhir.resources.STU3.library.Library")

LinkageType = create_fhir_type("LinkageType", "fhir.resources.STU3.linkage.Linkage")

LinkageItemType = create_fhir_type(
    "LinkageItemType", "fhir.resources.STU3.linkage.LinkageItem"
)

ListType = create_fhir_type("ListType", "fhir.resources.STU3.list.List")

ListEntryType = create_fhir_type("ListEntryType", "fhir.resources.STU3.list.ListEntry")

LocationType = create_fhir_type("LocationType", "fhir.resources.STU3.location.Location")

LocationPositionType = create_fhir_type(
    "LocationPositionType", "fhir.resources.STU3.location.LocationPosition"
)

MeasureType = create_fhir_type("MeasureType", "fhir.resources.STU3.measure.Measure")

MeasureGroupType = create_fhir_type(
    "MeasureGroupType", "fhir.resources.STU3.measure.MeasureGroup"
)

MeasureGroupPopulationType = create_fhir_type(
    "MeasureGroupPopulationType", "fhir.resources.STU3.measure.MeasureGroupPopulation"
)

MeasureGroupStratifierType = create_fhir_type(
    "MeasureGroupStratifierType", "fhir.resources.STU3.measure.MeasureGroupStratifier"
)

MeasureReportType = create_fhir_type(
    "MeasureReportType", "fhir.resources.STU3.measurereport.MeasureReport"
)

MeasureReportGroupType = create_fhir_type(
    "MeasureReportGroupType", "fhir.resources.STU3.measurereport.MeasureReportGroup"
)

MeasureReportGroupPopulationType = create_fhir_type(
    "MeasureReportGroupPopulationType",
    "fhir.resources.STU3.measurereport.MeasureReportGroupPopulation",
)

MeasureReportGroupStratifierType = create_fhir_type(
    "MeasureReportGroupStratifierType",
    "fhir.resources.STU3.measurereport.MeasureReportGroupStratifier",
)

MeasureReportGroupStratifierStratumType = create_fhir_type(
    "MeasureReportGroupStratifierStratumType",
    "fhir.resources.STU3.measurereport.MeasureReportGroupStratifierStratum",
)

MeasureReportGroupStratifierStratumPopulationType = create_fhir_type(
    "MeasureReportGroupStratifierStratumPopulationType",
    "fhir.resources.STU3.measurereport.MeasureReportGroupStratifierStratumPopulation",
)

MeasureSupplementalDataType = create_fhir_type(
    "MeasureSupplementalDataType", "fhir.resources.STU3.measure.MeasureSupplementalData"
)

MediaType = create_fhir_type("MediaType", "fhir.resources.STU3.media.Media")

MedicationType = create_fhir_type(
    "MedicationType", "fhir.resources.STU3.medication.Medication"
)

MedicationAdministrationType = create_fhir_type(
    "MedicationAdministrationType",
    "fhir.resources.STU3.medicationadministration.MedicationAdministration",
)

MedicationAdministrationDosageType = create_fhir_type(
    "MedicationAdministrationDosageType",
    "fhir.resources.STU3.medicationadministration.MedicationAdministrationDosage",
)

MedicationAdministrationPerformerType = create_fhir_type(
    "MedicationAdministrationPerformerType",
    "fhir.resources.STU3.medicationadministration.MedicationAdministrationPerformer",
)

MedicationDispenseType = create_fhir_type(
    "MedicationDispenseType",
    "fhir.resources.STU3.medicationdispense.MedicationDispense",
)

MedicationDispensePerformerType = create_fhir_type(
    "MedicationDispensePerformerType",
    "fhir.resources.STU3.medicationdispense.MedicationDispensePerformer",
)

MedicationDispenseSubstitutionType = create_fhir_type(
    "MedicationDispenseSubstitutionType",
    "fhir.resources.STU3.medicationdispense.MedicationDispenseSubstitution",
)

MedicationIngredientType = create_fhir_type(
    "MedicationIngredientType", "fhir.resources.STU3.medication.MedicationIngredient"
)

MedicationPackageType = create_fhir_type(
    "MedicationPackageType", "fhir.resources.STU3.medication.MedicationPackage"
)

MedicationPackageBatchType = create_fhir_type(
    "MedicationPackageBatchType",
    "fhir.resources.STU3.medication.MedicationPackageBatch",
)

MedicationPackageContentType = create_fhir_type(
    "MedicationPackageContentType",
    "fhir.resources.STU3.medication.MedicationPackageContent",
)

MedicationRequestType = create_fhir_type(
    "MedicationRequestType", "fhir.resources.STU3.medicationrequest.MedicationRequest"
)

MedicationRequestDispenseRequestType = create_fhir_type(
    "MedicationRequestDispenseRequestType",
    "fhir.resources.STU3.medicationrequest.MedicationRequestDispenseRequest",
)

MedicationRequestRequesterType = create_fhir_type(
    "MedicationRequestRequesterType",
    "fhir.resources.STU3.medicationrequest.MedicationRequestRequester",
)

MedicationRequestSubstitutionType = create_fhir_type(
    "MedicationRequestSubstitutionType",
    "fhir.resources.STU3.medicationrequest.MedicationRequestSubstitution",
)

MedicationStatementType = create_fhir_type(
    "MedicationStatementType",
    "fhir.resources.STU3.medicationstatement.MedicationStatement",
)

MessageDefinitionType = create_fhir_type(
    "MessageDefinitionType", "fhir.resources.STU3.messagedefinition.MessageDefinition"
)

MessageDefinitionAllowedResponseType = create_fhir_type(
    "MessageDefinitionAllowedResponseType",
    "fhir.resources.STU3.messagedefinition.MessageDefinitionAllowedResponse",
)

MessageDefinitionFocusType = create_fhir_type(
    "MessageDefinitionFocusType",
    "fhir.resources.STU3.messagedefinition.MessageDefinitionFocus",
)

MessageHeaderType = create_fhir_type(
    "MessageHeaderType", "fhir.resources.STU3.messageheader.MessageHeader"
)

MessageHeaderDestinationType = create_fhir_type(
    "MessageHeaderDestinationType",
    "fhir.resources.STU3.messageheader.MessageHeaderDestination",
)

MessageHeaderResponseType = create_fhir_type(
    "MessageHeaderResponseType",
    "fhir.resources.STU3.messageheader.MessageHeaderResponse",
)

MessageHeaderSourceType = create_fhir_type(
    "MessageHeaderSourceType", "fhir.resources.STU3.messageheader.MessageHeaderSource"
)

MetaType = create_fhir_type("MetaType", "fhir.resources.STU3.meta.Meta")

MetadataResourceType = create_fhir_type(
    "MetadataResourceType", "fhir.resources.STU3.metadataresource.MetadataResource"
)

MoneyType = create_fhir_type("MoneyType", "fhir.resources.STU3.money.Money")

NamingSystemType = create_fhir_type(
    "NamingSystemType", "fhir.resources.STU3.namingsystem.NamingSystem"
)

NamingSystemUniqueIdType = create_fhir_type(
    "NamingSystemUniqueIdType", "fhir.resources.STU3.namingsystem.NamingSystemUniqueId"
)

NarrativeType = create_fhir_type(
    "NarrativeType", "fhir.resources.STU3.narrative.Narrative"
)

NutritionOrderType = create_fhir_type(
    "NutritionOrderType", "fhir.resources.STU3.nutritionorder.NutritionOrder"
)

NutritionOrderEnteralFormulaType = create_fhir_type(
    "NutritionOrderEnteralFormulaType",
    "fhir.resources.STU3.nutritionorder.NutritionOrderEnteralFormula",
)

NutritionOrderEnteralFormulaAdministrationType = create_fhir_type(
    "NutritionOrderEnteralFormulaAdministrationType",
    "fhir.resources.STU3.nutritionorder.NutritionOrderEnteralFormulaAdministration",
)

NutritionOrderOralDietType = create_fhir_type(
    "NutritionOrderOralDietType",
    "fhir.resources.STU3.nutritionorder.NutritionOrderOralDiet",
)

NutritionOrderOralDietNutrientType = create_fhir_type(
    "NutritionOrderOralDietNutrientType",
    "fhir.resources.STU3.nutritionorder.NutritionOrderOralDietNutrient",
)

NutritionOrderOralDietTextureType = create_fhir_type(
    "NutritionOrderOralDietTextureType",
    "fhir.resources.STU3.nutritionorder.NutritionOrderOralDietTexture",
)

NutritionOrderSupplementType = create_fhir_type(
    "NutritionOrderSupplementType",
    "fhir.resources.STU3.nutritionorder.NutritionOrderSupplement",
)

ObservationType = create_fhir_type(
    "ObservationType", "fhir.resources.STU3.observation.Observation"
)

ObservationComponentType = create_fhir_type(
    "ObservationComponentType", "fhir.resources.STU3.observation.ObservationComponent"
)

ObservationReferenceRangeType = create_fhir_type(
    "ObservationReferenceRangeType",
    "fhir.resources.STU3.observation.ObservationReferenceRange",
)

ObservationRelatedType = create_fhir_type(
    "ObservationRelatedType", "fhir.resources.STU3.observation.ObservationRelated"
)

OperationDefinitionType = create_fhir_type(
    "OperationDefinitionType",
    "fhir.resources.STU3.operationdefinition.OperationDefinition",
)

OperationDefinitionOverloadType = create_fhir_type(
    "OperationDefinitionOverloadType",
    "fhir.resources.STU3.operationdefinition.OperationDefinitionOverload",
)

OperationDefinitionParameterType = create_fhir_type(
    "OperationDefinitionParameterType",
    "fhir.resources.STU3.operationdefinition.OperationDefinitionParameter",
)

OperationDefinitionParameterBindingType = create_fhir_type(
    "OperationDefinitionParameterBindingType",
    "fhir.resources.STU3.operationdefinition.OperationDefinitionParameterBinding",
)

OperationOutcomeType = create_fhir_type(
    "OperationOutcomeType", "fhir.resources.STU3.operationoutcome.OperationOutcome"
)

OperationOutcomeIssueType = create_fhir_type(
    "OperationOutcomeIssueType",
    "fhir.resources.STU3.operationoutcome.OperationOutcomeIssue",
)

OrganizationType = create_fhir_type(
    "OrganizationType", "fhir.resources.STU3.organization.Organization"
)

OrganizationContactType = create_fhir_type(
    "OrganizationContactType", "fhir.resources.STU3.organization.OrganizationContact"
)

ParameterDefinitionType = create_fhir_type(
    "ParameterDefinitionType",
    "fhir.resources.STU3.parameterdefinition.ParameterDefinition",
)

ParametersType = create_fhir_type(
    "ParametersType", "fhir.resources.STU3.parameters.Parameters"
)

ParametersParameterType = create_fhir_type(
    "ParametersParameterType", "fhir.resources.STU3.parameters.ParametersParameter"
)

PatientType = create_fhir_type("PatientType", "fhir.resources.STU3.patient.Patient")

PatientAnimalType = create_fhir_type(
    "PatientAnimalType", "fhir.resources.STU3.patient.PatientAnimal"
)

PatientCommunicationType = create_fhir_type(
    "PatientCommunicationType", "fhir.resources.STU3.patient.PatientCommunication"
)

PatientContactType = create_fhir_type(
    "PatientContactType", "fhir.resources.STU3.patient.PatientContact"
)

PatientLinkType = create_fhir_type(
    "PatientLinkType", "fhir.resources.STU3.patient.PatientLink"
)

PaymentNoticeType = create_fhir_type(
    "PaymentNoticeType", "fhir.resources.STU3.paymentnotice.PaymentNotice"
)

PaymentReconciliationType = create_fhir_type(
    "PaymentReconciliationType",
    "fhir.resources.STU3.paymentreconciliation.PaymentReconciliation",
)

PaymentReconciliationDetailType = create_fhir_type(
    "PaymentReconciliationDetailType",
    "fhir.resources.STU3.paymentreconciliation.PaymentReconciliationDetail",
)

PaymentReconciliationProcessNoteType = create_fhir_type(
    "PaymentReconciliationProcessNoteType",
    "fhir.resources.STU3.paymentreconciliation.PaymentReconciliationProcessNote",
)

PeriodType = create_fhir_type("PeriodType", "fhir.resources.STU3.period.Period")

PersonType = create_fhir_type("PersonType", "fhir.resources.STU3.person.Person")

PersonLinkType = create_fhir_type(
    "PersonLinkType", "fhir.resources.STU3.person.PersonLink"
)

PlanDefinitionType = create_fhir_type(
    "PlanDefinitionType", "fhir.resources.STU3.plandefinition.PlanDefinition"
)

PlanDefinitionActionType = create_fhir_type(
    "PlanDefinitionActionType",
    "fhir.resources.STU3.plandefinition.PlanDefinitionAction",
)

PlanDefinitionActionConditionType = create_fhir_type(
    "PlanDefinitionActionConditionType",
    "fhir.resources.STU3.plandefinition.PlanDefinitionActionCondition",
)

PlanDefinitionActionDynamicValueType = create_fhir_type(
    "PlanDefinitionActionDynamicValueType",
    "fhir.resources.STU3.plandefinition.PlanDefinitionActionDynamicValue",
)

PlanDefinitionActionParticipantType = create_fhir_type(
    "PlanDefinitionActionParticipantType",
    "fhir.resources.STU3.plandefinition.PlanDefinitionActionParticipant",
)

PlanDefinitionActionRelatedActionType = create_fhir_type(
    "PlanDefinitionActionRelatedActionType",
    "fhir.resources.STU3.plandefinition.PlanDefinitionActionRelatedAction",
)

PlanDefinitionGoalType = create_fhir_type(
    "PlanDefinitionGoalType", "fhir.resources.STU3.plandefinition.PlanDefinitionGoal"
)

PlanDefinitionGoalTargetType = create_fhir_type(
    "PlanDefinitionGoalTargetType",
    "fhir.resources.STU3.plandefinition.PlanDefinitionGoalTarget",
)

PractitionerType = create_fhir_type(
    "PractitionerType", "fhir.resources.STU3.practitioner.Practitioner"
)

PractitionerQualificationType = create_fhir_type(
    "PractitionerQualificationType",
    "fhir.resources.STU3.practitioner.PractitionerQualification",
)

PractitionerRoleType = create_fhir_type(
    "PractitionerRoleType", "fhir.resources.STU3.practitionerrole.PractitionerRole"
)

PractitionerRoleAvailableTimeType = create_fhir_type(
    "PractitionerRoleAvailableTimeType",
    "fhir.resources.STU3.practitionerrole.PractitionerRoleAvailableTime",
)

PractitionerRoleNotAvailableType = create_fhir_type(
    "PractitionerRoleNotAvailableType",
    "fhir.resources.STU3.practitionerrole.PractitionerRoleNotAvailable",
)

ProcedureType = create_fhir_type(
    "ProcedureType", "fhir.resources.STU3.procedure.Procedure"
)

ProcedureFocalDeviceType = create_fhir_type(
    "ProcedureFocalDeviceType", "fhir.resources.STU3.procedure.ProcedureFocalDevice"
)

ProcedurePerformerType = create_fhir_type(
    "ProcedurePerformerType", "fhir.resources.STU3.procedure.ProcedurePerformer"
)

ProcedureRequestType = create_fhir_type(
    "ProcedureRequestType", "fhir.resources.STU3.procedurerequest.ProcedureRequest"
)

ProcedureRequestRequesterType = create_fhir_type(
    "ProcedureRequestRequesterType",
    "fhir.resources.STU3.procedurerequest.ProcedureRequestRequester",
)

ProcessRequestType = create_fhir_type(
    "ProcessRequestType", "fhir.resources.STU3.processrequest.ProcessRequest"
)

ProcessRequestItemType = create_fhir_type(
    "ProcessRequestItemType", "fhir.resources.STU3.processrequest.ProcessRequestItem"
)

ProcessResponseType = create_fhir_type(
    "ProcessResponseType", "fhir.resources.STU3.processresponse.ProcessResponse"
)

ProcessResponseProcessNoteType = create_fhir_type(
    "ProcessResponseProcessNoteType",
    "fhir.resources.STU3.processresponse.ProcessResponseProcessNote",
)

ProvenanceType = create_fhir_type(
    "ProvenanceType", "fhir.resources.STU3.provenance.Provenance"
)

ProvenanceAgentType = create_fhir_type(
    "ProvenanceAgentType", "fhir.resources.STU3.provenance.ProvenanceAgent"
)

ProvenanceEntityType = create_fhir_type(
    "ProvenanceEntityType", "fhir.resources.STU3.provenance.ProvenanceEntity"
)

QuantityType = create_fhir_type("QuantityType", "fhir.resources.STU3.quantity.Quantity")

QuestionnaireType = create_fhir_type(
    "QuestionnaireType", "fhir.resources.STU3.questionnaire.Questionnaire"
)

QuestionnaireItemType = create_fhir_type(
    "QuestionnaireItemType", "fhir.resources.STU3.questionnaire.QuestionnaireItem"
)

QuestionnaireItemEnableWhenType = create_fhir_type(
    "QuestionnaireItemEnableWhenType",
    "fhir.resources.STU3.questionnaire.QuestionnaireItemEnableWhen",
)

QuestionnaireItemOptionType = create_fhir_type(
    "QuestionnaireItemOptionType",
    "fhir.resources.STU3.questionnaire.QuestionnaireItemOption",
)

QuestionnaireResponseType = create_fhir_type(
    "QuestionnaireResponseType",
    "fhir.resources.STU3.questionnaireresponse.QuestionnaireResponse",
)

QuestionnaireResponseItemType = create_fhir_type(
    "QuestionnaireResponseItemType",
    "fhir.resources.STU3.questionnaireresponse.QuestionnaireResponseItem",
)

QuestionnaireResponseItemAnswerType = create_fhir_type(
    "QuestionnaireResponseItemAnswerType",
    "fhir.resources.STU3.questionnaireresponse.QuestionnaireResponseItemAnswer",
)

RangeType = create_fhir_type("RangeType", "fhir.resources.STU3.range.Range")

RatioType = create_fhir_type("RatioType", "fhir.resources.STU3.ratio.Ratio")

ReferenceType = create_fhir_type(
    "ReferenceType", "fhir.resources.STU3.reference.Reference"
)

ReferralRequestType = create_fhir_type(
    "ReferralRequestType", "fhir.resources.STU3.referralrequest.ReferralRequest"
)

ReferralRequestRequesterType = create_fhir_type(
    "ReferralRequestRequesterType",
    "fhir.resources.STU3.referralrequest.ReferralRequestRequester",
)

RelatedArtifactType = create_fhir_type(
    "RelatedArtifactType", "fhir.resources.STU3.relatedartifact.RelatedArtifact"
)

RelatedPersonType = create_fhir_type(
    "RelatedPersonType", "fhir.resources.STU3.relatedperson.RelatedPerson"
)

RequestGroupType = create_fhir_type(
    "RequestGroupType", "fhir.resources.STU3.requestgroup.RequestGroup"
)

RequestGroupActionType = create_fhir_type(
    "RequestGroupActionType", "fhir.resources.STU3.requestgroup.RequestGroupAction"
)

RequestGroupActionConditionType = create_fhir_type(
    "RequestGroupActionConditionType",
    "fhir.resources.STU3.requestgroup.RequestGroupActionCondition",
)

RequestGroupActionRelatedActionType = create_fhir_type(
    "RequestGroupActionRelatedActionType",
    "fhir.resources.STU3.requestgroup.RequestGroupActionRelatedAction",
)

ResearchStudyType = create_fhir_type(
    "ResearchStudyType", "fhir.resources.STU3.researchstudy.ResearchStudy"
)

ResearchStudyArmType = create_fhir_type(
    "ResearchStudyArmType", "fhir.resources.STU3.researchstudy.ResearchStudyArm"
)

ResearchSubjectType = create_fhir_type(
    "ResearchSubjectType", "fhir.resources.STU3.researchsubject.ResearchSubject"
)

RiskAssessmentType = create_fhir_type(
    "RiskAssessmentType", "fhir.resources.STU3.riskassessment.RiskAssessment"
)

RiskAssessmentPredictionType = create_fhir_type(
    "RiskAssessmentPredictionType",
    "fhir.resources.STU3.riskassessment.RiskAssessmentPrediction",
)

SampledDataType = create_fhir_type(
    "SampledDataType", "fhir.resources.STU3.sampleddata.SampledData"
)

ScheduleType = create_fhir_type("ScheduleType", "fhir.resources.STU3.schedule.Schedule")

SearchParameterType = create_fhir_type(
    "SearchParameterType", "fhir.resources.STU3.searchparameter.SearchParameter"
)

SearchParameterComponentType = create_fhir_type(
    "SearchParameterComponentType",
    "fhir.resources.STU3.searchparameter.SearchParameterComponent",
)

SequenceType = create_fhir_type("SequenceType", "fhir.resources.STU3.sequence.Sequence")

SequenceQualityType = create_fhir_type(
    "SequenceQualityType", "fhir.resources.STU3.sequence.SequenceQuality"
)

SequenceReferenceSeqType = create_fhir_type(
    "SequenceReferenceSeqType", "fhir.resources.STU3.sequence.SequenceReferenceSeq"
)

SequenceRepositoryType = create_fhir_type(
    "SequenceRepositoryType", "fhir.resources.STU3.sequence.SequenceRepository"
)

SequenceVariantType = create_fhir_type(
    "SequenceVariantType", "fhir.resources.STU3.sequence.SequenceVariant"
)

ServiceDefinitionType = create_fhir_type(
    "ServiceDefinitionType", "fhir.resources.STU3.servicedefinition.ServiceDefinition"
)

SignatureType = create_fhir_type(
    "SignatureType", "fhir.resources.STU3.signature.Signature"
)

SlotType = create_fhir_type("SlotType", "fhir.resources.STU3.slot.Slot")

SpecimenType = create_fhir_type("SpecimenType", "fhir.resources.STU3.specimen.Specimen")

SpecimenCollectionType = create_fhir_type(
    "SpecimenCollectionType", "fhir.resources.STU3.specimen.SpecimenCollection"
)

SpecimenContainerType = create_fhir_type(
    "SpecimenContainerType", "fhir.resources.STU3.specimen.SpecimenContainer"
)

SpecimenProcessingType = create_fhir_type(
    "SpecimenProcessingType", "fhir.resources.STU3.specimen.SpecimenProcessing"
)

StructureDefinitionType = create_fhir_type(
    "StructureDefinitionType",
    "fhir.resources.STU3.structuredefinition.StructureDefinition",
)

StructureDefinitionDifferentialType = create_fhir_type(
    "StructureDefinitionDifferentialType",
    "fhir.resources.STU3.structuredefinition.StructureDefinitionDifferential",
)

StructureDefinitionMappingType = create_fhir_type(
    "StructureDefinitionMappingType",
    "fhir.resources.STU3.structuredefinition.StructureDefinitionMapping",
)

StructureDefinitionSnapshotType = create_fhir_type(
    "StructureDefinitionSnapshotType",
    "fhir.resources.STU3.structuredefinition.StructureDefinitionSnapshot",
)

StructureMapType = create_fhir_type(
    "StructureMapType", "fhir.resources.STU3.structuremap.StructureMap"
)

StructureMapGroupType = create_fhir_type(
    "StructureMapGroupType", "fhir.resources.STU3.structuremap.StructureMapGroup"
)

StructureMapGroupInputType = create_fhir_type(
    "StructureMapGroupInputType",
    "fhir.resources.STU3.structuremap.StructureMapGroupInput",
)

StructureMapGroupRuleType = create_fhir_type(
    "StructureMapGroupRuleType",
    "fhir.resources.STU3.structuremap.StructureMapGroupRule",
)

StructureMapGroupRuleDependentType = create_fhir_type(
    "StructureMapGroupRuleDependentType",
    "fhir.resources.STU3.structuremap.StructureMapGroupRuleDependent",
)

StructureMapGroupRuleSourceType = create_fhir_type(
    "StructureMapGroupRuleSourceType",
    "fhir.resources.STU3.structuremap.StructureMapGroupRuleSource",
)

StructureMapGroupRuleTargetType = create_fhir_type(
    "StructureMapGroupRuleTargetType",
    "fhir.resources.STU3.structuremap.StructureMapGroupRuleTarget",
)

StructureMapGroupRuleTargetParameterType = create_fhir_type(
    "StructureMapGroupRuleTargetParameterType",
    "fhir.resources.STU3.structuremap.StructureMapGroupRuleTargetParameter",
)

StructureMapStructureType = create_fhir_type(
    "StructureMapStructureType",
    "fhir.resources.STU3.structuremap.StructureMapStructure",
)

SubscriptionType = create_fhir_type(
    "SubscriptionType", "fhir.resources.STU3.subscription.Subscription"
)

SubscriptionChannelType = create_fhir_type(
    "SubscriptionChannelType", "fhir.resources.STU3.subscription.SubscriptionChannel"
)

SubstanceType = create_fhir_type(
    "SubstanceType", "fhir.resources.STU3.substance.Substance"
)

SubstanceIngredientType = create_fhir_type(
    "SubstanceIngredientType", "fhir.resources.STU3.substance.SubstanceIngredient"
)

SubstanceInstanceType = create_fhir_type(
    "SubstanceInstanceType", "fhir.resources.STU3.substance.SubstanceInstance"
)

SupplyDeliveryType = create_fhir_type(
    "SupplyDeliveryType", "fhir.resources.STU3.supplydelivery.SupplyDelivery"
)

SupplyDeliverySuppliedItemType = create_fhir_type(
    "SupplyDeliverySuppliedItemType",
    "fhir.resources.STU3.supplydelivery.SupplyDeliverySuppliedItem",
)

SupplyRequestType = create_fhir_type(
    "SupplyRequestType", "fhir.resources.STU3.supplyrequest.SupplyRequest"
)

SupplyRequestOrderedItemType = create_fhir_type(
    "SupplyRequestOrderedItemType",
    "fhir.resources.STU3.supplyrequest.SupplyRequestOrderedItem",
)

SupplyRequestRequesterType = create_fhir_type(
    "SupplyRequestRequesterType",
    "fhir.resources.STU3.supplyrequest.SupplyRequestRequester",
)

TaskType = create_fhir_type("TaskType", "fhir.resources.STU3.task.Task")

TaskInputType = create_fhir_type("TaskInputType", "fhir.resources.STU3.task.TaskInput")

TaskOutputType = create_fhir_type(
    "TaskOutputType", "fhir.resources.STU3.task.TaskOutput"
)

TaskRequesterType = create_fhir_type(
    "TaskRequesterType", "fhir.resources.STU3.task.TaskRequester"
)

TaskRestrictionType = create_fhir_type(
    "TaskRestrictionType", "fhir.resources.STU3.task.TaskRestriction"
)

TestReportType = create_fhir_type(
    "TestReportType", "fhir.resources.STU3.testreport.TestReport"
)

TestReportParticipantType = create_fhir_type(
    "TestReportParticipantType", "fhir.resources.STU3.testreport.TestReportParticipant"
)

TestReportSetupType = create_fhir_type(
    "TestReportSetupType", "fhir.resources.STU3.testreport.TestReportSetup"
)

TestReportSetupActionType = create_fhir_type(
    "TestReportSetupActionType", "fhir.resources.STU3.testreport.TestReportSetupAction"
)

TestReportSetupActionAssertType = create_fhir_type(
    "TestReportSetupActionAssertType",
    "fhir.resources.STU3.testreport.TestReportSetupActionAssert",
)

TestReportSetupActionOperationType = create_fhir_type(
    "TestReportSetupActionOperationType",
    "fhir.resources.STU3.testreport.TestReportSetupActionOperation",
)

TestReportTeardownType = create_fhir_type(
    "TestReportTeardownType", "fhir.resources.STU3.testreport.TestReportTeardown"
)

TestReportTeardownActionType = create_fhir_type(
    "TestReportTeardownActionType",
    "fhir.resources.STU3.testreport.TestReportTeardownAction",
)

TestReportTestType = create_fhir_type(
    "TestReportTestType", "fhir.resources.STU3.testreport.TestReportTest"
)

TestReportTestActionType = create_fhir_type(
    "TestReportTestActionType", "fhir.resources.STU3.testreport.TestReportTestAction"
)

TestScriptType = create_fhir_type(
    "TestScriptType", "fhir.resources.STU3.testscript.TestScript"
)

TestScriptDestinationType = create_fhir_type(
    "TestScriptDestinationType", "fhir.resources.STU3.testscript.TestScriptDestination"
)

TestScriptFixtureType = create_fhir_type(
    "TestScriptFixtureType", "fhir.resources.STU3.testscript.TestScriptFixture"
)

TestScriptMetadataType = create_fhir_type(
    "TestScriptMetadataType", "fhir.resources.STU3.testscript.TestScriptMetadata"
)

TestScriptMetadataCapabilityType = create_fhir_type(
    "TestScriptMetadataCapabilityType",
    "fhir.resources.STU3.testscript.TestScriptMetadataCapability",
)

TestScriptMetadataLinkType = create_fhir_type(
    "TestScriptMetadataLinkType",
    "fhir.resources.STU3.testscript.TestScriptMetadataLink",
)

TestScriptOriginType = create_fhir_type(
    "TestScriptOriginType", "fhir.resources.STU3.testscript.TestScriptOrigin"
)

TestScriptRuleType = create_fhir_type(
    "TestScriptRuleType", "fhir.resources.STU3.testscript.TestScriptRule"
)

TestScriptRuleParamType = create_fhir_type(
    "TestScriptRuleParamType", "fhir.resources.STU3.testscript.TestScriptRuleParam"
)

TestScriptRulesetType = create_fhir_type(
    "TestScriptRulesetType", "fhir.resources.STU3.testscript.TestScriptRuleset"
)

TestScriptRulesetRuleType = create_fhir_type(
    "TestScriptRulesetRuleType", "fhir.resources.STU3.testscript.TestScriptRulesetRule"
)

TestScriptRulesetRuleParamType = create_fhir_type(
    "TestScriptRulesetRuleParamType",
    "fhir.resources.STU3.testscript.TestScriptRulesetRuleParam",
)

TestScriptSetupType = create_fhir_type(
    "TestScriptSetupType", "fhir.resources.STU3.testscript.TestScriptSetup"
)

TestScriptSetupActionType = create_fhir_type(
    "TestScriptSetupActionType", "fhir.resources.STU3.testscript.TestScriptSetupAction"
)

TestScriptSetupActionAssertType = create_fhir_type(
    "TestScriptSetupActionAssertType",
    "fhir.resources.STU3.testscript.TestScriptSetupActionAssert",
)

TestScriptSetupActionAssertRuleType = create_fhir_type(
    "TestScriptSetupActionAssertRuleType",
    "fhir.resources.STU3.testscript.TestScriptSetupActionAssertRule",
)

TestScriptSetupActionAssertRuleParamType = create_fhir_type(
    "TestScriptSetupActionAssertRuleParamType",
    "fhir.resources.STU3.testscript.TestScriptSetupActionAssertRuleParam",
)

TestScriptSetupActionAssertRulesetType = create_fhir_type(
    "TestScriptSetupActionAssertRulesetType",
    "fhir.resources.STU3.testscript.TestScriptSetupActionAssertRuleset",
)

TestScriptSetupActionAssertRulesetRuleType = create_fhir_type(
    "TestScriptSetupActionAssertRulesetRuleType",
    "fhir.resources.STU3.testscript.TestScriptSetupActionAssertRulesetRule",
)

TestScriptSetupActionAssertRulesetRuleParamType = create_fhir_type(
    "TestScriptSetupActionAssertRulesetRuleParamType",
    "fhir.resources.STU3.testscript.TestScriptSetupActionAssertRulesetRuleParam",
)

TestScriptSetupActionOperationType = create_fhir_type(
    "TestScriptSetupActionOperationType",
    "fhir.resources.STU3.testscript.TestScriptSetupActionOperation",
)

TestScriptSetupActionOperationRequestHeaderType = create_fhir_type(
    "TestScriptSetupActionOperationRequestHeaderType",
    "fhir.resources.STU3.testscript.TestScriptSetupActionOperationRequestHeader",
)

TestScriptTeardownType = create_fhir_type(
    "TestScriptTeardownType", "fhir.resources.STU3.testscript.TestScriptTeardown"
)

TestScriptTeardownActionType = create_fhir_type(
    "TestScriptTeardownActionType",
    "fhir.resources.STU3.testscript.TestScriptTeardownAction",
)

TestScriptTestType = create_fhir_type(
    "TestScriptTestType", "fhir.resources.STU3.testscript.TestScriptTest"
)

TestScriptTestActionType = create_fhir_type(
    "TestScriptTestActionType", "fhir.resources.STU3.testscript.TestScriptTestAction"
)

TestScriptVariableType = create_fhir_type(
    "TestScriptVariableType", "fhir.resources.STU3.testscript.TestScriptVariable"
)

TimingType = create_fhir_type("TimingType", "fhir.resources.STU3.timing.Timing")

TimingRepeatType = create_fhir_type(
    "TimingRepeatType", "fhir.resources.STU3.timing.TimingRepeat"
)

TriggerDefinitionType = create_fhir_type(
    "TriggerDefinitionType", "fhir.resources.STU3.triggerdefinition.TriggerDefinition"
)

UsageContextType = create_fhir_type(
    "UsageContextType", "fhir.resources.STU3.usagecontext.UsageContext"
)

ValueSetType = create_fhir_type("ValueSetType", "fhir.resources.STU3.valueset.ValueSet")

ValueSetComposeType = create_fhir_type(
    "ValueSetComposeType", "fhir.resources.STU3.valueset.ValueSetCompose"
)

ValueSetComposeIncludeType = create_fhir_type(
    "ValueSetComposeIncludeType", "fhir.resources.STU3.valueset.ValueSetComposeInclude"
)

ValueSetComposeIncludeConceptType = create_fhir_type(
    "ValueSetComposeIncludeConceptType",
    "fhir.resources.STU3.valueset.ValueSetComposeIncludeConcept",
)

ValueSetComposeIncludeConceptDesignationType = create_fhir_type(
    "ValueSetComposeIncludeConceptDesignationType",
    "fhir.resources.STU3.valueset.ValueSetComposeIncludeConceptDesignation",
)

ValueSetComposeIncludeFilterType = create_fhir_type(
    "ValueSetComposeIncludeFilterType",
    "fhir.resources.STU3.valueset.ValueSetComposeIncludeFilter",
)

ValueSetExpansionType = create_fhir_type(
    "ValueSetExpansionType", "fhir.resources.STU3.valueset.ValueSetExpansion"
)

ValueSetExpansionContainsType = create_fhir_type(
    "ValueSetExpansionContainsType",
    "fhir.resources.STU3.valueset.ValueSetExpansionContains",
)

ValueSetExpansionParameterType = create_fhir_type(
    "ValueSetExpansionParameterType",
    "fhir.resources.STU3.valueset.ValueSetExpansionParameter",
)

VisionPrescriptionType = create_fhir_type(
    "VisionPrescriptionType",
    "fhir.resources.STU3.visionprescription.VisionPrescription",
)

VisionPrescriptionDispenseType = create_fhir_type(
    "VisionPrescriptionDispenseType",
    "fhir.resources.STU3.visionprescription.VisionPrescriptionDispense",
)

__all__ = [
    "BooleanType",
    "StringType",
    "Base64BinaryType",
    "CodeType",
    "IdType",
    "IntegerType",
    "Integer64Type",
    "DecimalType",
    "UnsignedIntType",
    "PositiveIntType",
    "CanonicalType",
    "UriType",
    "OidType",
    "UuidType",
    "UrlType",
    "MarkdownType",
    "XhtmlType",
    "DateType",
    "DateTimeType",
    "InstantType",
    "TimeType",
    "FHIRPrimitiveExtensionType",
    "AccountType",
    "AccountCoverageType",
    "AccountGuarantorType",
    "ActivityDefinitionType",
    "ActivityDefinitionDynamicValueType",
    "ActivityDefinitionParticipantType",
    "AddressType",
    "AdverseEventType",
    "AdverseEventSuspectEntityType",
    "AgeType",
    "AllergyIntoleranceType",
    "AllergyIntoleranceReactionType",
    "AnnotationType",
    "AppointmentType",
    "AppointmentParticipantType",
    "AppointmentResponseType",
    "AttachmentType",
    "AuditEventType",
    "AuditEventAgentType",
    "AuditEventAgentNetworkType",
    "AuditEventEntityType",
    "AuditEventEntityDetailType",
    "AuditEventSourceType",
    "BackboneElementType",
    "BasicType",
    "BinaryType",
    "BodySiteType",
    "BundleType",
    "BundleEntryType",
    "BundleEntryRequestType",
    "BundleEntryResponseType",
    "BundleEntrySearchType",
    "BundleLinkType",
    "CapabilityStatementType",
    "CapabilityStatementDocumentType",
    "CapabilityStatementImplementationType",
    "CapabilityStatementMessagingType",
    "CapabilityStatementMessagingEndpointType",
    "CapabilityStatementMessagingEventType",
    "CapabilityStatementMessagingSupportedMessageType",
    "CapabilityStatementRestType",
    "CapabilityStatementRestInteractionType",
    "CapabilityStatementRestOperationType",
    "CapabilityStatementRestResourceType",
    "CapabilityStatementRestResourceInteractionType",
    "CapabilityStatementRestResourceSearchParamType",
    "CapabilityStatementRestSecurityType",
    "CapabilityStatementRestSecurityCertificateType",
    "CapabilityStatementSoftwareType",
    "CarePlanType",
    "CarePlanActivityType",
    "CarePlanActivityDetailType",
    "CareTeamType",
    "CareTeamParticipantType",
    "ChargeItemType",
    "ChargeItemParticipantType",
    "ClaimType",
    "ClaimAccidentType",
    "ClaimCareTeamType",
    "ClaimDiagnosisType",
    "ClaimInformationType",
    "ClaimInsuranceType",
    "ClaimItemType",
    "ClaimItemDetailType",
    "ClaimItemDetailSubDetailType",
    "ClaimPayeeType",
    "ClaimProcedureType",
    "ClaimRelatedType",
    "ClaimResponseType",
    "ClaimResponseAddItemType",
    "ClaimResponseAddItemDetailType",
    "ClaimResponseErrorType",
    "ClaimResponseInsuranceType",
    "ClaimResponseItemType",
    "ClaimResponseItemAdjudicationType",
    "ClaimResponseItemDetailType",
    "ClaimResponseItemDetailSubDetailType",
    "ClaimResponsePaymentType",
    "ClaimResponseProcessNoteType",
    "ClinicalImpressionType",
    "ClinicalImpressionFindingType",
    "ClinicalImpressionInvestigationType",
    "CodeSystemType",
    "CodeSystemConceptType",
    "CodeSystemConceptDesignationType",
    "CodeSystemConceptPropertyType",
    "CodeSystemFilterType",
    "CodeSystemPropertyType",
    "CodeableConceptType",
    "CodingType",
    "CommunicationType",
    "CommunicationPayloadType",
    "CommunicationRequestType",
    "CommunicationRequestPayloadType",
    "CommunicationRequestRequesterType",
    "CompartmentDefinitionType",
    "CompartmentDefinitionResourceType",
    "CompositionType",
    "CompositionAttesterType",
    "CompositionEventType",
    "CompositionRelatesToType",
    "CompositionSectionType",
    "ConceptMapType",
    "ConceptMapGroupType",
    "ConceptMapGroupElementType",
    "ConceptMapGroupElementTargetType",
    "ConceptMapGroupElementTargetDependsOnType",
    "ConceptMapGroupUnmappedType",
    "ConditionType",
    "ConditionEvidenceType",
    "ConditionStageType",
    "ConsentType",
    "ConsentActorType",
    "ConsentDataType",
    "ConsentExceptType",
    "ConsentExceptActorType",
    "ConsentExceptDataType",
    "ConsentPolicyType",
    "ContactDetailType",
    "ContactPointType",
    "ContractType",
    "ContractAgentType",
    "ContractFriendlyType",
    "ContractLegalType",
    "ContractRuleType",
    "ContractSignerType",
    "ContractTermType",
    "ContractTermAgentType",
    "ContractTermValuedItemType",
    "ContractValuedItemType",
    "ContributorType",
    "CountType",
    "CoverageType",
    "CoverageGroupingType",
    "DataElementType",
    "DataElementMappingType",
    "DataRequirementType",
    "DataRequirementCodeFilterType",
    "DataRequirementDateFilterType",
    "DetectedIssueType",
    "DetectedIssueMitigationType",
    "DeviceType",
    "DeviceComponentType",
    "DeviceComponentProductionSpecificationType",
    "DeviceMetricType",
    "DeviceMetricCalibrationType",
    "DeviceRequestType",
    "DeviceRequestRequesterType",
    "DeviceUdiType",
    "DeviceUseStatementType",
    "DiagnosticReportType",
    "DiagnosticReportImageType",
    "DiagnosticReportPerformerType",
    "DistanceType",
    "DocumentManifestType",
    "DocumentManifestContentType",
    "DocumentManifestRelatedType",
    "DocumentReferenceType",
    "DocumentReferenceContentType",
    "DocumentReferenceContextType",
    "DocumentReferenceContextRelatedType",
    "DocumentReferenceRelatesToType",
    "DomainResourceType",
    "DosageType",
    "DurationType",
    "ElementType",
    "ElementDefinitionType",
    "ElementDefinitionBaseType",
    "ElementDefinitionBindingType",
    "ElementDefinitionConstraintType",
    "ElementDefinitionExampleType",
    "ElementDefinitionMappingType",
    "ElementDefinitionSlicingType",
    "ElementDefinitionSlicingDiscriminatorType",
    "ElementDefinitionTypeType",
    "EligibilityRequestType",
    "EligibilityResponseType",
    "EligibilityResponseErrorType",
    "EligibilityResponseInsuranceType",
    "EligibilityResponseInsuranceBenefitBalanceType",
    "EligibilityResponseInsuranceBenefitBalanceFinancialType",
    "EncounterType",
    "EncounterClassHistoryType",
    "EncounterDiagnosisType",
    "EncounterHospitalizationType",
    "EncounterLocationType",
    "EncounterParticipantType",
    "EncounterStatusHistoryType",
    "EndpointType",
    "EnrollmentRequestType",
    "EnrollmentResponseType",
    "EpisodeOfCareType",
    "EpisodeOfCareDiagnosisType",
    "EpisodeOfCareStatusHistoryType",
    "ExpansionProfileType",
    "ExpansionProfileDesignationType",
    "ExpansionProfileDesignationExcludeType",
    "ExpansionProfileDesignationExcludeDesignationType",
    "ExpansionProfileDesignationIncludeType",
    "ExpansionProfileDesignationIncludeDesignationType",
    "ExpansionProfileExcludedSystemType",
    "ExpansionProfileFixedVersionType",
    "ExplanationOfBenefitType",
    "ExplanationOfBenefitAccidentType",
    "ExplanationOfBenefitAddItemType",
    "ExplanationOfBenefitAddItemDetailType",
    "ExplanationOfBenefitBenefitBalanceType",
    "ExplanationOfBenefitBenefitBalanceFinancialType",
    "ExplanationOfBenefitCareTeamType",
    "ExplanationOfBenefitDiagnosisType",
    "ExplanationOfBenefitInformationType",
    "ExplanationOfBenefitInsuranceType",
    "ExplanationOfBenefitItemType",
    "ExplanationOfBenefitItemAdjudicationType",
    "ExplanationOfBenefitItemDetailType",
    "ExplanationOfBenefitItemDetailSubDetailType",
    "ExplanationOfBenefitPayeeType",
    "ExplanationOfBenefitPaymentType",
    "ExplanationOfBenefitProcedureType",
    "ExplanationOfBenefitProcessNoteType",
    "ExplanationOfBenefitRelatedType",
    "ExtensionType",
    "FamilyMemberHistoryType",
    "FamilyMemberHistoryConditionType",
    "FlagType",
    "GoalType",
    "GoalTargetType",
    "GraphDefinitionType",
    "GraphDefinitionLinkType",
    "GraphDefinitionLinkTargetType",
    "GraphDefinitionLinkTargetCompartmentType",
    "GroupType",
    "GroupCharacteristicType",
    "GroupMemberType",
    "GuidanceResponseType",
    "HealthcareServiceType",
    "HealthcareServiceAvailableTimeType",
    "HealthcareServiceNotAvailableType",
    "HumanNameType",
    "IdentifierType",
    "ImagingManifestType",
    "ImagingManifestStudyType",
    "ImagingManifestStudySeriesType",
    "ImagingManifestStudySeriesInstanceType",
    "ImagingStudyType",
    "ImagingStudySeriesType",
    "ImagingStudySeriesInstanceType",
    "ImmunizationType",
    "ImmunizationExplanationType",
    "ImmunizationPractitionerType",
    "ImmunizationReactionType",
    "ImmunizationRecommendationType",
    "ImmunizationRecommendationRecommendationType",
    "ImmunizationRecommendationRecommendationDateCriterionType",
    "ImmunizationRecommendationRecommendationProtocolType",
    "ImmunizationVaccinationProtocolType",
    "ImplementationGuideType",
    "ImplementationGuideDependencyType",
    "ImplementationGuideGlobalType",
    "ImplementationGuidePackageType",
    "ImplementationGuidePackageResourceType",
    "ImplementationGuidePageType",
    "LibraryType",
    "LinkageType",
    "LinkageItemType",
    "ListType",
    "ListEntryType",
    "LocationType",
    "LocationPositionType",
    "MeasureType",
    "MeasureGroupType",
    "MeasureGroupPopulationType",
    "MeasureGroupStratifierType",
    "MeasureReportType",
    "MeasureReportGroupType",
    "MeasureReportGroupPopulationType",
    "MeasureReportGroupStratifierType",
    "MeasureReportGroupStratifierStratumType",
    "MeasureReportGroupStratifierStratumPopulationType",
    "MeasureSupplementalDataType",
    "MediaType",
    "MedicationType",
    "MedicationAdministrationType",
    "MedicationAdministrationDosageType",
    "MedicationAdministrationPerformerType",
    "MedicationDispenseType",
    "MedicationDispensePerformerType",
    "MedicationDispenseSubstitutionType",
    "MedicationIngredientType",
    "MedicationPackageType",
    "MedicationPackageBatchType",
    "MedicationPackageContentType",
    "MedicationRequestType",
    "MedicationRequestDispenseRequestType",
    "MedicationRequestRequesterType",
    "MedicationRequestSubstitutionType",
    "MedicationStatementType",
    "MessageDefinitionType",
    "MessageDefinitionAllowedResponseType",
    "MessageDefinitionFocusType",
    "MessageHeaderType",
    "MessageHeaderDestinationType",
    "MessageHeaderResponseType",
    "MessageHeaderSourceType",
    "MetaType",
    "MetadataResourceType",
    "MoneyType",
    "NamingSystemType",
    "NamingSystemUniqueIdType",
    "NarrativeType",
    "NutritionOrderType",
    "NutritionOrderEnteralFormulaType",
    "NutritionOrderEnteralFormulaAdministrationType",
    "NutritionOrderOralDietType",
    "NutritionOrderOralDietNutrientType",
    "NutritionOrderOralDietTextureType",
    "NutritionOrderSupplementType",
    "ObservationType",
    "ObservationComponentType",
    "ObservationReferenceRangeType",
    "ObservationRelatedType",
    "OperationDefinitionType",
    "OperationDefinitionOverloadType",
    "OperationDefinitionParameterType",
    "OperationDefinitionParameterBindingType",
    "OperationOutcomeType",
    "OperationOutcomeIssueType",
    "OrganizationType",
    "OrganizationContactType",
    "ParameterDefinitionType",
    "ParametersType",
    "ParametersParameterType",
    "PatientType",
    "PatientAnimalType",
    "PatientCommunicationType",
    "PatientContactType",
    "PatientLinkType",
    "PaymentNoticeType",
    "PaymentReconciliationType",
    "PaymentReconciliationDetailType",
    "PaymentReconciliationProcessNoteType",
    "PeriodType",
    "PersonType",
    "PersonLinkType",
    "PlanDefinitionType",
    "PlanDefinitionActionType",
    "PlanDefinitionActionConditionType",
    "PlanDefinitionActionDynamicValueType",
    "PlanDefinitionActionParticipantType",
    "PlanDefinitionActionRelatedActionType",
    "PlanDefinitionGoalType",
    "PlanDefinitionGoalTargetType",
    "PractitionerType",
    "PractitionerQualificationType",
    "PractitionerRoleType",
    "PractitionerRoleAvailableTimeType",
    "PractitionerRoleNotAvailableType",
    "ProcedureType",
    "ProcedureFocalDeviceType",
    "ProcedurePerformerType",
    "ProcedureRequestType",
    "ProcedureRequestRequesterType",
    "ProcessRequestType",
    "ProcessRequestItemType",
    "ProcessResponseType",
    "ProcessResponseProcessNoteType",
    "ProvenanceType",
    "ProvenanceAgentType",
    "ProvenanceEntityType",
    "QuantityType",
    "QuestionnaireType",
    "QuestionnaireItemType",
    "QuestionnaireItemEnableWhenType",
    "QuestionnaireItemOptionType",
    "QuestionnaireResponseType",
    "QuestionnaireResponseItemType",
    "QuestionnaireResponseItemAnswerType",
    "RangeType",
    "RatioType",
    "ReferenceType",
    "ReferralRequestType",
    "ReferralRequestRequesterType",
    "RelatedArtifactType",
    "RelatedPersonType",
    "RequestGroupType",
    "RequestGroupActionType",
    "RequestGroupActionConditionType",
    "RequestGroupActionRelatedActionType",
    "ResearchStudyType",
    "ResearchStudyArmType",
    "ResearchSubjectType",
    "ResourceType",
    "RiskAssessmentType",
    "RiskAssessmentPredictionType",
    "SampledDataType",
    "ScheduleType",
    "SearchParameterType",
    "SearchParameterComponentType",
    "SequenceType",
    "SequenceQualityType",
    "SequenceReferenceSeqType",
    "SequenceRepositoryType",
    "SequenceVariantType",
    "ServiceDefinitionType",
    "SignatureType",
    "SlotType",
    "SpecimenType",
    "SpecimenCollectionType",
    "SpecimenContainerType",
    "SpecimenProcessingType",
    "StructureDefinitionType",
    "StructureDefinitionDifferentialType",
    "StructureDefinitionMappingType",
    "StructureDefinitionSnapshotType",
    "StructureMapType",
    "StructureMapGroupType",
    "StructureMapGroupInputType",
    "StructureMapGroupRuleType",
    "StructureMapGroupRuleDependentType",
    "StructureMapGroupRuleSourceType",
    "StructureMapGroupRuleTargetType",
    "StructureMapGroupRuleTargetParameterType",
    "StructureMapStructureType",
    "SubscriptionType",
    "SubscriptionChannelType",
    "SubstanceType",
    "SubstanceIngredientType",
    "SubstanceInstanceType",
    "SupplyDeliveryType",
    "SupplyDeliverySuppliedItemType",
    "SupplyRequestType",
    "SupplyRequestOrderedItemType",
    "SupplyRequestRequesterType",
    "TaskType",
    "TaskInputType",
    "TaskOutputType",
    "TaskRequesterType",
    "TaskRestrictionType",
    "TestReportType",
    "TestReportParticipantType",
    "TestReportSetupType",
    "TestReportSetupActionType",
    "TestReportSetupActionAssertType",
    "TestReportSetupActionOperationType",
    "TestReportTeardownType",
    "TestReportTeardownActionType",
    "TestReportTestType",
    "TestReportTestActionType",
    "TestScriptType",
    "TestScriptDestinationType",
    "TestScriptFixtureType",
    "TestScriptMetadataType",
    "TestScriptMetadataCapabilityType",
    "TestScriptMetadataLinkType",
    "TestScriptOriginType",
    "TestScriptRuleType",
    "TestScriptRuleParamType",
    "TestScriptRulesetType",
    "TestScriptRulesetRuleType",
    "TestScriptRulesetRuleParamType",
    "TestScriptSetupType",
    "TestScriptSetupActionType",
    "TestScriptSetupActionAssertType",
    "TestScriptSetupActionAssertRuleType",
    "TestScriptSetupActionAssertRuleParamType",
    "TestScriptSetupActionAssertRulesetType",
    "TestScriptSetupActionAssertRulesetRuleType",
    "TestScriptSetupActionAssertRulesetRuleParamType",
    "TestScriptSetupActionOperationType",
    "TestScriptSetupActionOperationRequestHeaderType",
    "TestScriptTeardownType",
    "TestScriptTeardownActionType",
    "TestScriptTestType",
    "TestScriptTestActionType",
    "TestScriptVariableType",
    "TimingType",
    "TimingRepeatType",
    "TriggerDefinitionType",
    "UsageContextType",
    "ValueSetType",
    "ValueSetComposeType",
    "ValueSetComposeIncludeType",
    "ValueSetComposeIncludeConceptType",
    "ValueSetComposeIncludeConceptDesignationType",
    "ValueSetComposeIncludeFilterType",
    "ValueSetExpansionType",
    "ValueSetExpansionContainsType",
    "ValueSetExpansionParameterType",
    "VisionPrescriptionType",
    "VisionPrescriptionDispenseType",
]
