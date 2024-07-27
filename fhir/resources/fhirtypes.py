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
    "fhir.resources.fhirprimitiveextension.FHIRPrimitiveExtension",
)

ElementType = create_fhir_element_or_resource_type(
    "ElementType", "fhir.resources.element.Element"
)

ResourceType = create_fhir_element_or_resource_type(
    "ResourceType", "fhir.resources.resource.Resource"
)
AccountType = create_fhir_type("AccountType", "fhir.resources.account.Account")

AccountBalanceType = create_fhir_type(
    "AccountBalanceType", "fhir.resources.account.AccountBalance"
)

AccountCoverageType = create_fhir_type(
    "AccountCoverageType", "fhir.resources.account.AccountCoverage"
)

AccountDiagnosisType = create_fhir_type(
    "AccountDiagnosisType", "fhir.resources.account.AccountDiagnosis"
)

AccountGuarantorType = create_fhir_type(
    "AccountGuarantorType", "fhir.resources.account.AccountGuarantor"
)

AccountProcedureType = create_fhir_type(
    "AccountProcedureType", "fhir.resources.account.AccountProcedure"
)

AccountRelatedAccountType = create_fhir_type(
    "AccountRelatedAccountType", "fhir.resources.account.AccountRelatedAccount"
)

ActivityDefinitionType = create_fhir_type(
    "ActivityDefinitionType", "fhir.resources.activitydefinition.ActivityDefinition"
)

ActivityDefinitionDynamicValueType = create_fhir_type(
    "ActivityDefinitionDynamicValueType",
    "fhir.resources.activitydefinition.ActivityDefinitionDynamicValue",
)

ActivityDefinitionParticipantType = create_fhir_type(
    "ActivityDefinitionParticipantType",
    "fhir.resources.activitydefinition.ActivityDefinitionParticipant",
)

ActorDefinitionType = create_fhir_type(
    "ActorDefinitionType", "fhir.resources.actordefinition.ActorDefinition"
)

AddressType = create_fhir_type("AddressType", "fhir.resources.address.Address")

AdministrableProductDefinitionType = create_fhir_type(
    "AdministrableProductDefinitionType",
    "fhir.resources.administrableproductdefinition.AdministrableProductDefinition",
)

AdministrableProductDefinitionPropertyType = create_fhir_type(
    "AdministrableProductDefinitionPropertyType",
    "fhir.resources.administrableproductdefinition.AdministrableProductDefinitionProperty",
)

AdministrableProductDefinitionRouteOfAdministrationType = create_fhir_type(
    "AdministrableProductDefinitionRouteOfAdministrationType",
    "fhir.resources.administrableproductdefinition.AdministrableProductDefinitionRouteOfAdministration",
)

AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesType = create_fhir_type(
    "AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesType",
    "fhir.resources.administrableproductdefinition.AdministrableProductDefinitionRouteOfAdministrationTargetSpecies",
)

AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriodType = create_fhir_type(
    "AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriodType",
    "fhir.resources.administrableproductdefinition.AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod",
)

AdverseEventType = create_fhir_type(
    "AdverseEventType", "fhir.resources.adverseevent.AdverseEvent"
)

AdverseEventContributingFactorType = create_fhir_type(
    "AdverseEventContributingFactorType",
    "fhir.resources.adverseevent.AdverseEventContributingFactor",
)

AdverseEventMitigatingActionType = create_fhir_type(
    "AdverseEventMitigatingActionType",
    "fhir.resources.adverseevent.AdverseEventMitigatingAction",
)

AdverseEventParticipantType = create_fhir_type(
    "AdverseEventParticipantType", "fhir.resources.adverseevent.AdverseEventParticipant"
)

AdverseEventPreventiveActionType = create_fhir_type(
    "AdverseEventPreventiveActionType",
    "fhir.resources.adverseevent.AdverseEventPreventiveAction",
)

AdverseEventSupportingInfoType = create_fhir_type(
    "AdverseEventSupportingInfoType",
    "fhir.resources.adverseevent.AdverseEventSupportingInfo",
)

AdverseEventSuspectEntityType = create_fhir_type(
    "AdverseEventSuspectEntityType",
    "fhir.resources.adverseevent.AdverseEventSuspectEntity",
)

AdverseEventSuspectEntityCausalityType = create_fhir_type(
    "AdverseEventSuspectEntityCausalityType",
    "fhir.resources.adverseevent.AdverseEventSuspectEntityCausality",
)

AgeType = create_fhir_type("AgeType", "fhir.resources.age.Age")

AllergyIntoleranceType = create_fhir_type(
    "AllergyIntoleranceType", "fhir.resources.allergyintolerance.AllergyIntolerance"
)

AllergyIntoleranceParticipantType = create_fhir_type(
    "AllergyIntoleranceParticipantType",
    "fhir.resources.allergyintolerance.AllergyIntoleranceParticipant",
)

AllergyIntoleranceReactionType = create_fhir_type(
    "AllergyIntoleranceReactionType",
    "fhir.resources.allergyintolerance.AllergyIntoleranceReaction",
)

AnnotationType = create_fhir_type(
    "AnnotationType", "fhir.resources.annotation.Annotation"
)

AppointmentType = create_fhir_type(
    "AppointmentType", "fhir.resources.appointment.Appointment"
)

AppointmentParticipantType = create_fhir_type(
    "AppointmentParticipantType", "fhir.resources.appointment.AppointmentParticipant"
)

AppointmentRecurrenceTemplateType = create_fhir_type(
    "AppointmentRecurrenceTemplateType",
    "fhir.resources.appointment.AppointmentRecurrenceTemplate",
)

AppointmentRecurrenceTemplateMonthlyTemplateType = create_fhir_type(
    "AppointmentRecurrenceTemplateMonthlyTemplateType",
    "fhir.resources.appointment.AppointmentRecurrenceTemplateMonthlyTemplate",
)

AppointmentRecurrenceTemplateWeeklyTemplateType = create_fhir_type(
    "AppointmentRecurrenceTemplateWeeklyTemplateType",
    "fhir.resources.appointment.AppointmentRecurrenceTemplateWeeklyTemplate",
)

AppointmentRecurrenceTemplateYearlyTemplateType = create_fhir_type(
    "AppointmentRecurrenceTemplateYearlyTemplateType",
    "fhir.resources.appointment.AppointmentRecurrenceTemplateYearlyTemplate",
)

AppointmentResponseType = create_fhir_type(
    "AppointmentResponseType", "fhir.resources.appointmentresponse.AppointmentResponse"
)

ArtifactAssessmentType = create_fhir_type(
    "ArtifactAssessmentType", "fhir.resources.artifactassessment.ArtifactAssessment"
)

ArtifactAssessmentContentType = create_fhir_type(
    "ArtifactAssessmentContentType",
    "fhir.resources.artifactassessment.ArtifactAssessmentContent",
)

AttachmentType = create_fhir_type(
    "AttachmentType", "fhir.resources.attachment.Attachment"
)

AuditEventType = create_fhir_type(
    "AuditEventType", "fhir.resources.auditevent.AuditEvent"
)

AuditEventAgentType = create_fhir_type(
    "AuditEventAgentType", "fhir.resources.auditevent.AuditEventAgent"
)

AuditEventEntityType = create_fhir_type(
    "AuditEventEntityType", "fhir.resources.auditevent.AuditEventEntity"
)

AuditEventEntityDetailType = create_fhir_type(
    "AuditEventEntityDetailType", "fhir.resources.auditevent.AuditEventEntityDetail"
)

AuditEventOutcomeType = create_fhir_type(
    "AuditEventOutcomeType", "fhir.resources.auditevent.AuditEventOutcome"
)

AuditEventSourceType = create_fhir_type(
    "AuditEventSourceType", "fhir.resources.auditevent.AuditEventSource"
)

AvailabilityType = create_fhir_type(
    "AvailabilityType", "fhir.resources.availability.Availability"
)

AvailabilityAvailableTimeType = create_fhir_type(
    "AvailabilityAvailableTimeType",
    "fhir.resources.availability.AvailabilityAvailableTime",
)

AvailabilityNotAvailableTimeType = create_fhir_type(
    "AvailabilityNotAvailableTimeType",
    "fhir.resources.availability.AvailabilityNotAvailableTime",
)

BackboneElementType = create_fhir_type(
    "BackboneElementType", "fhir.resources.backboneelement.BackboneElement"
)

BackboneTypeType = create_fhir_type(
    "BackboneTypeType", "fhir.resources.backbonetype.BackboneType"
)

BaseType = create_fhir_type("BaseType", "fhir.resources.base.Base")

BasicType = create_fhir_type("BasicType", "fhir.resources.basic.Basic")

BinaryType = create_fhir_type("BinaryType", "fhir.resources.binary.Binary")

BiologicallyDerivedProductType = create_fhir_type(
    "BiologicallyDerivedProductType",
    "fhir.resources.biologicallyderivedproduct.BiologicallyDerivedProduct",
)

BiologicallyDerivedProductCollectionType = create_fhir_type(
    "BiologicallyDerivedProductCollectionType",
    "fhir.resources.biologicallyderivedproduct.BiologicallyDerivedProductCollection",
)

BiologicallyDerivedProductDispenseType = create_fhir_type(
    "BiologicallyDerivedProductDispenseType",
    "fhir.resources.biologicallyderivedproductdispense.BiologicallyDerivedProductDispense",
)

BiologicallyDerivedProductDispensePerformerType = create_fhir_type(
    "BiologicallyDerivedProductDispensePerformerType",
    "fhir.resources.biologicallyderivedproductdispense.BiologicallyDerivedProductDispensePerformer",
)

BiologicallyDerivedProductPropertyType = create_fhir_type(
    "BiologicallyDerivedProductPropertyType",
    "fhir.resources.biologicallyderivedproduct.BiologicallyDerivedProductProperty",
)

BodyStructureType = create_fhir_type(
    "BodyStructureType", "fhir.resources.bodystructure.BodyStructure"
)

BodyStructureIncludedStructureType = create_fhir_type(
    "BodyStructureIncludedStructureType",
    "fhir.resources.bodystructure.BodyStructureIncludedStructure",
)

BodyStructureIncludedStructureBodyLandmarkOrientationType = create_fhir_type(
    "BodyStructureIncludedStructureBodyLandmarkOrientationType",
    "fhir.resources.bodystructure.BodyStructureIncludedStructureBodyLandmarkOrientation",
)

BodyStructureIncludedStructureBodyLandmarkOrientationDistanceFromLandmarkType = create_fhir_type(
    "BodyStructureIncludedStructureBodyLandmarkOrientationDistanceFromLandmarkType",
    "fhir.resources.bodystructure.BodyStructureIncludedStructureBodyLandmarkOrientationDistanceFromLandmark",
)

BundleType = create_fhir_type("BundleType", "fhir.resources.bundle.Bundle")

BundleEntryType = create_fhir_type(
    "BundleEntryType", "fhir.resources.bundle.BundleEntry"
)

BundleEntryRequestType = create_fhir_type(
    "BundleEntryRequestType", "fhir.resources.bundle.BundleEntryRequest"
)

BundleEntryResponseType = create_fhir_type(
    "BundleEntryResponseType", "fhir.resources.bundle.BundleEntryResponse"
)

BundleEntrySearchType = create_fhir_type(
    "BundleEntrySearchType", "fhir.resources.bundle.BundleEntrySearch"
)

BundleLinkType = create_fhir_type("BundleLinkType", "fhir.resources.bundle.BundleLink")

CanonicalResourceType = create_fhir_type(
    "CanonicalResourceType", "fhir.resources.canonicalresource.CanonicalResource"
)

CapabilityStatementType = create_fhir_type(
    "CapabilityStatementType", "fhir.resources.capabilitystatement.CapabilityStatement"
)

CapabilityStatementDocumentType = create_fhir_type(
    "CapabilityStatementDocumentType",
    "fhir.resources.capabilitystatement.CapabilityStatementDocument",
)

CapabilityStatementImplementationType = create_fhir_type(
    "CapabilityStatementImplementationType",
    "fhir.resources.capabilitystatement.CapabilityStatementImplementation",
)

CapabilityStatementMessagingType = create_fhir_type(
    "CapabilityStatementMessagingType",
    "fhir.resources.capabilitystatement.CapabilityStatementMessaging",
)

CapabilityStatementMessagingEndpointType = create_fhir_type(
    "CapabilityStatementMessagingEndpointType",
    "fhir.resources.capabilitystatement.CapabilityStatementMessagingEndpoint",
)

CapabilityStatementMessagingSupportedMessageType = create_fhir_type(
    "CapabilityStatementMessagingSupportedMessageType",
    "fhir.resources.capabilitystatement.CapabilityStatementMessagingSupportedMessage",
)

CapabilityStatementRestType = create_fhir_type(
    "CapabilityStatementRestType",
    "fhir.resources.capabilitystatement.CapabilityStatementRest",
)

CapabilityStatementRestInteractionType = create_fhir_type(
    "CapabilityStatementRestInteractionType",
    "fhir.resources.capabilitystatement.CapabilityStatementRestInteraction",
)

CapabilityStatementRestResourceType = create_fhir_type(
    "CapabilityStatementRestResourceType",
    "fhir.resources.capabilitystatement.CapabilityStatementRestResource",
)

CapabilityStatementRestResourceInteractionType = create_fhir_type(
    "CapabilityStatementRestResourceInteractionType",
    "fhir.resources.capabilitystatement.CapabilityStatementRestResourceInteraction",
)

CapabilityStatementRestResourceOperationType = create_fhir_type(
    "CapabilityStatementRestResourceOperationType",
    "fhir.resources.capabilitystatement.CapabilityStatementRestResourceOperation",
)

CapabilityStatementRestResourceSearchParamType = create_fhir_type(
    "CapabilityStatementRestResourceSearchParamType",
    "fhir.resources.capabilitystatement.CapabilityStatementRestResourceSearchParam",
)

CapabilityStatementRestSecurityType = create_fhir_type(
    "CapabilityStatementRestSecurityType",
    "fhir.resources.capabilitystatement.CapabilityStatementRestSecurity",
)

CapabilityStatementSoftwareType = create_fhir_type(
    "CapabilityStatementSoftwareType",
    "fhir.resources.capabilitystatement.CapabilityStatementSoftware",
)

CarePlanType = create_fhir_type("CarePlanType", "fhir.resources.careplan.CarePlan")

CarePlanActivityType = create_fhir_type(
    "CarePlanActivityType", "fhir.resources.careplan.CarePlanActivity"
)

CareTeamType = create_fhir_type("CareTeamType", "fhir.resources.careteam.CareTeam")

CareTeamParticipantType = create_fhir_type(
    "CareTeamParticipantType", "fhir.resources.careteam.CareTeamParticipant"
)

ChargeItemType = create_fhir_type(
    "ChargeItemType", "fhir.resources.chargeitem.ChargeItem"
)

ChargeItemDefinitionType = create_fhir_type(
    "ChargeItemDefinitionType",
    "fhir.resources.chargeitemdefinition.ChargeItemDefinition",
)

ChargeItemDefinitionApplicabilityType = create_fhir_type(
    "ChargeItemDefinitionApplicabilityType",
    "fhir.resources.chargeitemdefinition.ChargeItemDefinitionApplicability",
)

ChargeItemDefinitionPropertyGroupType = create_fhir_type(
    "ChargeItemDefinitionPropertyGroupType",
    "fhir.resources.chargeitemdefinition.ChargeItemDefinitionPropertyGroup",
)

ChargeItemPerformerType = create_fhir_type(
    "ChargeItemPerformerType", "fhir.resources.chargeitem.ChargeItemPerformer"
)

CitationType = create_fhir_type("CitationType", "fhir.resources.citation.Citation")

CitationCitedArtifactType = create_fhir_type(
    "CitationCitedArtifactType", "fhir.resources.citation.CitationCitedArtifact"
)

CitationCitedArtifactAbstractType = create_fhir_type(
    "CitationCitedArtifactAbstractType",
    "fhir.resources.citation.CitationCitedArtifactAbstract",
)

CitationCitedArtifactClassificationType = create_fhir_type(
    "CitationCitedArtifactClassificationType",
    "fhir.resources.citation.CitationCitedArtifactClassification",
)

CitationCitedArtifactContributorshipType = create_fhir_type(
    "CitationCitedArtifactContributorshipType",
    "fhir.resources.citation.CitationCitedArtifactContributorship",
)

CitationCitedArtifactContributorshipEntryType = create_fhir_type(
    "CitationCitedArtifactContributorshipEntryType",
    "fhir.resources.citation.CitationCitedArtifactContributorshipEntry",
)

CitationCitedArtifactContributorshipEntryContributionInstanceType = create_fhir_type(
    "CitationCitedArtifactContributorshipEntryContributionInstanceType",
    "fhir.resources.citation.CitationCitedArtifactContributorshipEntryContributionInstance",
)

CitationCitedArtifactContributorshipSummaryType = create_fhir_type(
    "CitationCitedArtifactContributorshipSummaryType",
    "fhir.resources.citation.CitationCitedArtifactContributorshipSummary",
)

CitationCitedArtifactPartType = create_fhir_type(
    "CitationCitedArtifactPartType", "fhir.resources.citation.CitationCitedArtifactPart"
)

CitationCitedArtifactPublicationFormType = create_fhir_type(
    "CitationCitedArtifactPublicationFormType",
    "fhir.resources.citation.CitationCitedArtifactPublicationForm",
)

CitationCitedArtifactPublicationFormPublishedInType = create_fhir_type(
    "CitationCitedArtifactPublicationFormPublishedInType",
    "fhir.resources.citation.CitationCitedArtifactPublicationFormPublishedIn",
)

CitationCitedArtifactRelatesToType = create_fhir_type(
    "CitationCitedArtifactRelatesToType",
    "fhir.resources.citation.CitationCitedArtifactRelatesTo",
)

CitationCitedArtifactStatusDateType = create_fhir_type(
    "CitationCitedArtifactStatusDateType",
    "fhir.resources.citation.CitationCitedArtifactStatusDate",
)

CitationCitedArtifactTitleType = create_fhir_type(
    "CitationCitedArtifactTitleType",
    "fhir.resources.citation.CitationCitedArtifactTitle",
)

CitationCitedArtifactVersionType = create_fhir_type(
    "CitationCitedArtifactVersionType",
    "fhir.resources.citation.CitationCitedArtifactVersion",
)

CitationCitedArtifactWebLocationType = create_fhir_type(
    "CitationCitedArtifactWebLocationType",
    "fhir.resources.citation.CitationCitedArtifactWebLocation",
)

CitationClassificationType = create_fhir_type(
    "CitationClassificationType", "fhir.resources.citation.CitationClassification"
)

CitationStatusDateType = create_fhir_type(
    "CitationStatusDateType", "fhir.resources.citation.CitationStatusDate"
)

CitationSummaryType = create_fhir_type(
    "CitationSummaryType", "fhir.resources.citation.CitationSummary"
)

ClaimType = create_fhir_type("ClaimType", "fhir.resources.claim.Claim")

ClaimAccidentType = create_fhir_type(
    "ClaimAccidentType", "fhir.resources.claim.ClaimAccident"
)

ClaimCareTeamType = create_fhir_type(
    "ClaimCareTeamType", "fhir.resources.claim.ClaimCareTeam"
)

ClaimDiagnosisType = create_fhir_type(
    "ClaimDiagnosisType", "fhir.resources.claim.ClaimDiagnosis"
)

ClaimEventType = create_fhir_type("ClaimEventType", "fhir.resources.claim.ClaimEvent")

ClaimInsuranceType = create_fhir_type(
    "ClaimInsuranceType", "fhir.resources.claim.ClaimInsurance"
)

ClaimItemType = create_fhir_type("ClaimItemType", "fhir.resources.claim.ClaimItem")

ClaimItemBodySiteType = create_fhir_type(
    "ClaimItemBodySiteType", "fhir.resources.claim.ClaimItemBodySite"
)

ClaimItemDetailType = create_fhir_type(
    "ClaimItemDetailType", "fhir.resources.claim.ClaimItemDetail"
)

ClaimItemDetailSubDetailType = create_fhir_type(
    "ClaimItemDetailSubDetailType", "fhir.resources.claim.ClaimItemDetailSubDetail"
)

ClaimPayeeType = create_fhir_type("ClaimPayeeType", "fhir.resources.claim.ClaimPayee")

ClaimProcedureType = create_fhir_type(
    "ClaimProcedureType", "fhir.resources.claim.ClaimProcedure"
)

ClaimRelatedType = create_fhir_type(
    "ClaimRelatedType", "fhir.resources.claim.ClaimRelated"
)

ClaimResponseType = create_fhir_type(
    "ClaimResponseType", "fhir.resources.claimresponse.ClaimResponse"
)

ClaimResponseAddItemType = create_fhir_type(
    "ClaimResponseAddItemType", "fhir.resources.claimresponse.ClaimResponseAddItem"
)

ClaimResponseAddItemBodySiteType = create_fhir_type(
    "ClaimResponseAddItemBodySiteType",
    "fhir.resources.claimresponse.ClaimResponseAddItemBodySite",
)

ClaimResponseAddItemDetailType = create_fhir_type(
    "ClaimResponseAddItemDetailType",
    "fhir.resources.claimresponse.ClaimResponseAddItemDetail",
)

ClaimResponseAddItemDetailSubDetailType = create_fhir_type(
    "ClaimResponseAddItemDetailSubDetailType",
    "fhir.resources.claimresponse.ClaimResponseAddItemDetailSubDetail",
)

ClaimResponseErrorType = create_fhir_type(
    "ClaimResponseErrorType", "fhir.resources.claimresponse.ClaimResponseError"
)

ClaimResponseEventType = create_fhir_type(
    "ClaimResponseEventType", "fhir.resources.claimresponse.ClaimResponseEvent"
)

ClaimResponseInsuranceType = create_fhir_type(
    "ClaimResponseInsuranceType", "fhir.resources.claimresponse.ClaimResponseInsurance"
)

ClaimResponseItemType = create_fhir_type(
    "ClaimResponseItemType", "fhir.resources.claimresponse.ClaimResponseItem"
)

ClaimResponseItemAdjudicationType = create_fhir_type(
    "ClaimResponseItemAdjudicationType",
    "fhir.resources.claimresponse.ClaimResponseItemAdjudication",
)

ClaimResponseItemDetailType = create_fhir_type(
    "ClaimResponseItemDetailType",
    "fhir.resources.claimresponse.ClaimResponseItemDetail",
)

ClaimResponseItemDetailSubDetailType = create_fhir_type(
    "ClaimResponseItemDetailSubDetailType",
    "fhir.resources.claimresponse.ClaimResponseItemDetailSubDetail",
)

ClaimResponseItemReviewOutcomeType = create_fhir_type(
    "ClaimResponseItemReviewOutcomeType",
    "fhir.resources.claimresponse.ClaimResponseItemReviewOutcome",
)

ClaimResponsePaymentType = create_fhir_type(
    "ClaimResponsePaymentType", "fhir.resources.claimresponse.ClaimResponsePayment"
)

ClaimResponseProcessNoteType = create_fhir_type(
    "ClaimResponseProcessNoteType",
    "fhir.resources.claimresponse.ClaimResponseProcessNote",
)

ClaimResponseTotalType = create_fhir_type(
    "ClaimResponseTotalType", "fhir.resources.claimresponse.ClaimResponseTotal"
)

ClaimSupportingInfoType = create_fhir_type(
    "ClaimSupportingInfoType", "fhir.resources.claim.ClaimSupportingInfo"
)

ClinicalImpressionType = create_fhir_type(
    "ClinicalImpressionType", "fhir.resources.clinicalimpression.ClinicalImpression"
)

ClinicalImpressionFindingType = create_fhir_type(
    "ClinicalImpressionFindingType",
    "fhir.resources.clinicalimpression.ClinicalImpressionFinding",
)

ClinicalUseDefinitionType = create_fhir_type(
    "ClinicalUseDefinitionType",
    "fhir.resources.clinicalusedefinition.ClinicalUseDefinition",
)

ClinicalUseDefinitionContraindicationType = create_fhir_type(
    "ClinicalUseDefinitionContraindicationType",
    "fhir.resources.clinicalusedefinition.ClinicalUseDefinitionContraindication",
)

ClinicalUseDefinitionContraindicationOtherTherapyType = create_fhir_type(
    "ClinicalUseDefinitionContraindicationOtherTherapyType",
    "fhir.resources.clinicalusedefinition.ClinicalUseDefinitionContraindicationOtherTherapy",
)

ClinicalUseDefinitionIndicationType = create_fhir_type(
    "ClinicalUseDefinitionIndicationType",
    "fhir.resources.clinicalusedefinition.ClinicalUseDefinitionIndication",
)

ClinicalUseDefinitionInteractionType = create_fhir_type(
    "ClinicalUseDefinitionInteractionType",
    "fhir.resources.clinicalusedefinition.ClinicalUseDefinitionInteraction",
)

ClinicalUseDefinitionInteractionInteractantType = create_fhir_type(
    "ClinicalUseDefinitionInteractionInteractantType",
    "fhir.resources.clinicalusedefinition.ClinicalUseDefinitionInteractionInteractant",
)

ClinicalUseDefinitionUndesirableEffectType = create_fhir_type(
    "ClinicalUseDefinitionUndesirableEffectType",
    "fhir.resources.clinicalusedefinition.ClinicalUseDefinitionUndesirableEffect",
)

ClinicalUseDefinitionWarningType = create_fhir_type(
    "ClinicalUseDefinitionWarningType",
    "fhir.resources.clinicalusedefinition.ClinicalUseDefinitionWarning",
)

CodeSystemType = create_fhir_type(
    "CodeSystemType", "fhir.resources.codesystem.CodeSystem"
)

CodeSystemConceptType = create_fhir_type(
    "CodeSystemConceptType", "fhir.resources.codesystem.CodeSystemConcept"
)

CodeSystemConceptDesignationType = create_fhir_type(
    "CodeSystemConceptDesignationType",
    "fhir.resources.codesystem.CodeSystemConceptDesignation",
)

CodeSystemConceptPropertyType = create_fhir_type(
    "CodeSystemConceptPropertyType",
    "fhir.resources.codesystem.CodeSystemConceptProperty",
)

CodeSystemFilterType = create_fhir_type(
    "CodeSystemFilterType", "fhir.resources.codesystem.CodeSystemFilter"
)

CodeSystemPropertyType = create_fhir_type(
    "CodeSystemPropertyType", "fhir.resources.codesystem.CodeSystemProperty"
)

CodeableConceptType = create_fhir_type(
    "CodeableConceptType", "fhir.resources.codeableconcept.CodeableConcept"
)

CodeableReferenceType = create_fhir_type(
    "CodeableReferenceType", "fhir.resources.codeablereference.CodeableReference"
)

CodingType = create_fhir_type("CodingType", "fhir.resources.coding.Coding")

CommunicationType = create_fhir_type(
    "CommunicationType", "fhir.resources.communication.Communication"
)

CommunicationPayloadType = create_fhir_type(
    "CommunicationPayloadType", "fhir.resources.communication.CommunicationPayload"
)

CommunicationRequestType = create_fhir_type(
    "CommunicationRequestType",
    "fhir.resources.communicationrequest.CommunicationRequest",
)

CommunicationRequestPayloadType = create_fhir_type(
    "CommunicationRequestPayloadType",
    "fhir.resources.communicationrequest.CommunicationRequestPayload",
)

CompartmentDefinitionType = create_fhir_type(
    "CompartmentDefinitionType",
    "fhir.resources.compartmentdefinition.CompartmentDefinition",
)

CompartmentDefinitionResourceType = create_fhir_type(
    "CompartmentDefinitionResourceType",
    "fhir.resources.compartmentdefinition.CompartmentDefinitionResource",
)

CompositionType = create_fhir_type(
    "CompositionType", "fhir.resources.composition.Composition"
)

CompositionAttesterType = create_fhir_type(
    "CompositionAttesterType", "fhir.resources.composition.CompositionAttester"
)

CompositionEventType = create_fhir_type(
    "CompositionEventType", "fhir.resources.composition.CompositionEvent"
)

CompositionSectionType = create_fhir_type(
    "CompositionSectionType", "fhir.resources.composition.CompositionSection"
)

ConceptMapType = create_fhir_type(
    "ConceptMapType", "fhir.resources.conceptmap.ConceptMap"
)

ConceptMapAdditionalAttributeType = create_fhir_type(
    "ConceptMapAdditionalAttributeType",
    "fhir.resources.conceptmap.ConceptMapAdditionalAttribute",
)

ConceptMapGroupType = create_fhir_type(
    "ConceptMapGroupType", "fhir.resources.conceptmap.ConceptMapGroup"
)

ConceptMapGroupElementType = create_fhir_type(
    "ConceptMapGroupElementType", "fhir.resources.conceptmap.ConceptMapGroupElement"
)

ConceptMapGroupElementTargetType = create_fhir_type(
    "ConceptMapGroupElementTargetType",
    "fhir.resources.conceptmap.ConceptMapGroupElementTarget",
)

ConceptMapGroupElementTargetDependsOnType = create_fhir_type(
    "ConceptMapGroupElementTargetDependsOnType",
    "fhir.resources.conceptmap.ConceptMapGroupElementTargetDependsOn",
)

ConceptMapGroupElementTargetPropertyType = create_fhir_type(
    "ConceptMapGroupElementTargetPropertyType",
    "fhir.resources.conceptmap.ConceptMapGroupElementTargetProperty",
)

ConceptMapGroupUnmappedType = create_fhir_type(
    "ConceptMapGroupUnmappedType", "fhir.resources.conceptmap.ConceptMapGroupUnmapped"
)

ConceptMapPropertyType = create_fhir_type(
    "ConceptMapPropertyType", "fhir.resources.conceptmap.ConceptMapProperty"
)

ConditionType = create_fhir_type("ConditionType", "fhir.resources.condition.Condition")

ConditionDefinitionType = create_fhir_type(
    "ConditionDefinitionType", "fhir.resources.conditiondefinition.ConditionDefinition"
)

ConditionDefinitionMedicationType = create_fhir_type(
    "ConditionDefinitionMedicationType",
    "fhir.resources.conditiondefinition.ConditionDefinitionMedication",
)

ConditionDefinitionObservationType = create_fhir_type(
    "ConditionDefinitionObservationType",
    "fhir.resources.conditiondefinition.ConditionDefinitionObservation",
)

ConditionDefinitionPlanType = create_fhir_type(
    "ConditionDefinitionPlanType",
    "fhir.resources.conditiondefinition.ConditionDefinitionPlan",
)

ConditionDefinitionPreconditionType = create_fhir_type(
    "ConditionDefinitionPreconditionType",
    "fhir.resources.conditiondefinition.ConditionDefinitionPrecondition",
)

ConditionDefinitionQuestionnaireType = create_fhir_type(
    "ConditionDefinitionQuestionnaireType",
    "fhir.resources.conditiondefinition.ConditionDefinitionQuestionnaire",
)

ConditionParticipantType = create_fhir_type(
    "ConditionParticipantType", "fhir.resources.condition.ConditionParticipant"
)

ConditionStageType = create_fhir_type(
    "ConditionStageType", "fhir.resources.condition.ConditionStage"
)

ConsentType = create_fhir_type("ConsentType", "fhir.resources.consent.Consent")

ConsentPolicyBasisType = create_fhir_type(
    "ConsentPolicyBasisType", "fhir.resources.consent.ConsentPolicyBasis"
)

ConsentProvisionType = create_fhir_type(
    "ConsentProvisionType", "fhir.resources.consent.ConsentProvision"
)

ConsentProvisionActorType = create_fhir_type(
    "ConsentProvisionActorType", "fhir.resources.consent.ConsentProvisionActor"
)

ConsentProvisionDataType = create_fhir_type(
    "ConsentProvisionDataType", "fhir.resources.consent.ConsentProvisionData"
)

ConsentVerificationType = create_fhir_type(
    "ConsentVerificationType", "fhir.resources.consent.ConsentVerification"
)

ContactDetailType = create_fhir_type(
    "ContactDetailType", "fhir.resources.contactdetail.ContactDetail"
)

ContactPointType = create_fhir_type(
    "ContactPointType", "fhir.resources.contactpoint.ContactPoint"
)

ContractType = create_fhir_type("ContractType", "fhir.resources.contract.Contract")

ContractContentDefinitionType = create_fhir_type(
    "ContractContentDefinitionType", "fhir.resources.contract.ContractContentDefinition"
)

ContractFriendlyType = create_fhir_type(
    "ContractFriendlyType", "fhir.resources.contract.ContractFriendly"
)

ContractLegalType = create_fhir_type(
    "ContractLegalType", "fhir.resources.contract.ContractLegal"
)

ContractRuleType = create_fhir_type(
    "ContractRuleType", "fhir.resources.contract.ContractRule"
)

ContractSignerType = create_fhir_type(
    "ContractSignerType", "fhir.resources.contract.ContractSigner"
)

ContractTermType = create_fhir_type(
    "ContractTermType", "fhir.resources.contract.ContractTerm"
)

ContractTermActionType = create_fhir_type(
    "ContractTermActionType", "fhir.resources.contract.ContractTermAction"
)

ContractTermActionSubjectType = create_fhir_type(
    "ContractTermActionSubjectType", "fhir.resources.contract.ContractTermActionSubject"
)

ContractTermAssetType = create_fhir_type(
    "ContractTermAssetType", "fhir.resources.contract.ContractTermAsset"
)

ContractTermAssetContextType = create_fhir_type(
    "ContractTermAssetContextType", "fhir.resources.contract.ContractTermAssetContext"
)

ContractTermAssetValuedItemType = create_fhir_type(
    "ContractTermAssetValuedItemType",
    "fhir.resources.contract.ContractTermAssetValuedItem",
)

ContractTermOfferType = create_fhir_type(
    "ContractTermOfferType", "fhir.resources.contract.ContractTermOffer"
)

ContractTermOfferAnswerType = create_fhir_type(
    "ContractTermOfferAnswerType", "fhir.resources.contract.ContractTermOfferAnswer"
)

ContractTermOfferPartyType = create_fhir_type(
    "ContractTermOfferPartyType", "fhir.resources.contract.ContractTermOfferParty"
)

ContractTermSecurityLabelType = create_fhir_type(
    "ContractTermSecurityLabelType", "fhir.resources.contract.ContractTermSecurityLabel"
)

ContributorType = create_fhir_type(
    "ContributorType", "fhir.resources.contributor.Contributor"
)

CountType = create_fhir_type("CountType", "fhir.resources.count.Count")

CoverageType = create_fhir_type("CoverageType", "fhir.resources.coverage.Coverage")

CoverageClassType = create_fhir_type(
    "CoverageClassType", "fhir.resources.coverage.CoverageClass"
)

CoverageCostToBeneficiaryType = create_fhir_type(
    "CoverageCostToBeneficiaryType", "fhir.resources.coverage.CoverageCostToBeneficiary"
)

CoverageCostToBeneficiaryExceptionType = create_fhir_type(
    "CoverageCostToBeneficiaryExceptionType",
    "fhir.resources.coverage.CoverageCostToBeneficiaryException",
)

CoverageEligibilityRequestType = create_fhir_type(
    "CoverageEligibilityRequestType",
    "fhir.resources.coverageeligibilityrequest.CoverageEligibilityRequest",
)

CoverageEligibilityRequestEventType = create_fhir_type(
    "CoverageEligibilityRequestEventType",
    "fhir.resources.coverageeligibilityrequest.CoverageEligibilityRequestEvent",
)

CoverageEligibilityRequestInsuranceType = create_fhir_type(
    "CoverageEligibilityRequestInsuranceType",
    "fhir.resources.coverageeligibilityrequest.CoverageEligibilityRequestInsurance",
)

CoverageEligibilityRequestItemType = create_fhir_type(
    "CoverageEligibilityRequestItemType",
    "fhir.resources.coverageeligibilityrequest.CoverageEligibilityRequestItem",
)

CoverageEligibilityRequestItemDiagnosisType = create_fhir_type(
    "CoverageEligibilityRequestItemDiagnosisType",
    "fhir.resources.coverageeligibilityrequest.CoverageEligibilityRequestItemDiagnosis",
)

CoverageEligibilityRequestSupportingInfoType = create_fhir_type(
    "CoverageEligibilityRequestSupportingInfoType",
    "fhir.resources.coverageeligibilityrequest.CoverageEligibilityRequestSupportingInfo",
)

CoverageEligibilityResponseType = create_fhir_type(
    "CoverageEligibilityResponseType",
    "fhir.resources.coverageeligibilityresponse.CoverageEligibilityResponse",
)

CoverageEligibilityResponseErrorType = create_fhir_type(
    "CoverageEligibilityResponseErrorType",
    "fhir.resources.coverageeligibilityresponse.CoverageEligibilityResponseError",
)

CoverageEligibilityResponseEventType = create_fhir_type(
    "CoverageEligibilityResponseEventType",
    "fhir.resources.coverageeligibilityresponse.CoverageEligibilityResponseEvent",
)

CoverageEligibilityResponseInsuranceType = create_fhir_type(
    "CoverageEligibilityResponseInsuranceType",
    "fhir.resources.coverageeligibilityresponse.CoverageEligibilityResponseInsurance",
)

CoverageEligibilityResponseInsuranceItemType = create_fhir_type(
    "CoverageEligibilityResponseInsuranceItemType",
    "fhir.resources.coverageeligibilityresponse.CoverageEligibilityResponseInsuranceItem",
)

CoverageEligibilityResponseInsuranceItemBenefitType = create_fhir_type(
    "CoverageEligibilityResponseInsuranceItemBenefitType",
    "fhir.resources.coverageeligibilityresponse.CoverageEligibilityResponseInsuranceItemBenefit",
)

CoveragePaymentByType = create_fhir_type(
    "CoveragePaymentByType", "fhir.resources.coverage.CoveragePaymentBy"
)

DataRequirementType = create_fhir_type(
    "DataRequirementType", "fhir.resources.datarequirement.DataRequirement"
)

DataRequirementCodeFilterType = create_fhir_type(
    "DataRequirementCodeFilterType",
    "fhir.resources.datarequirement.DataRequirementCodeFilter",
)

DataRequirementDateFilterType = create_fhir_type(
    "DataRequirementDateFilterType",
    "fhir.resources.datarequirement.DataRequirementDateFilter",
)

DataRequirementSortType = create_fhir_type(
    "DataRequirementSortType", "fhir.resources.datarequirement.DataRequirementSort"
)

DataRequirementValueFilterType = create_fhir_type(
    "DataRequirementValueFilterType",
    "fhir.resources.datarequirement.DataRequirementValueFilter",
)

DataTypeType = create_fhir_type("DataTypeType", "fhir.resources.datatype.DataType")

DetectedIssueType = create_fhir_type(
    "DetectedIssueType", "fhir.resources.detectedissue.DetectedIssue"
)

DetectedIssueEvidenceType = create_fhir_type(
    "DetectedIssueEvidenceType", "fhir.resources.detectedissue.DetectedIssueEvidence"
)

DetectedIssueMitigationType = create_fhir_type(
    "DetectedIssueMitigationType",
    "fhir.resources.detectedissue.DetectedIssueMitigation",
)

DeviceType = create_fhir_type("DeviceType", "fhir.resources.device.Device")

DeviceAssociationType = create_fhir_type(
    "DeviceAssociationType", "fhir.resources.deviceassociation.DeviceAssociation"
)

DeviceAssociationOperationType = create_fhir_type(
    "DeviceAssociationOperationType",
    "fhir.resources.deviceassociation.DeviceAssociationOperation",
)

DeviceConformsToType = create_fhir_type(
    "DeviceConformsToType", "fhir.resources.device.DeviceConformsTo"
)

DeviceDefinitionType = create_fhir_type(
    "DeviceDefinitionType", "fhir.resources.devicedefinition.DeviceDefinition"
)

DeviceDefinitionChargeItemType = create_fhir_type(
    "DeviceDefinitionChargeItemType",
    "fhir.resources.devicedefinition.DeviceDefinitionChargeItem",
)

DeviceDefinitionClassificationType = create_fhir_type(
    "DeviceDefinitionClassificationType",
    "fhir.resources.devicedefinition.DeviceDefinitionClassification",
)

DeviceDefinitionConformsToType = create_fhir_type(
    "DeviceDefinitionConformsToType",
    "fhir.resources.devicedefinition.DeviceDefinitionConformsTo",
)

DeviceDefinitionCorrectiveActionType = create_fhir_type(
    "DeviceDefinitionCorrectiveActionType",
    "fhir.resources.devicedefinition.DeviceDefinitionCorrectiveAction",
)

DeviceDefinitionDeviceNameType = create_fhir_type(
    "DeviceDefinitionDeviceNameType",
    "fhir.resources.devicedefinition.DeviceDefinitionDeviceName",
)

DeviceDefinitionGuidelineType = create_fhir_type(
    "DeviceDefinitionGuidelineType",
    "fhir.resources.devicedefinition.DeviceDefinitionGuideline",
)

DeviceDefinitionHasPartType = create_fhir_type(
    "DeviceDefinitionHasPartType",
    "fhir.resources.devicedefinition.DeviceDefinitionHasPart",
)

DeviceDefinitionLinkType = create_fhir_type(
    "DeviceDefinitionLinkType", "fhir.resources.devicedefinition.DeviceDefinitionLink"
)

DeviceDefinitionMaterialType = create_fhir_type(
    "DeviceDefinitionMaterialType",
    "fhir.resources.devicedefinition.DeviceDefinitionMaterial",
)

DeviceDefinitionPackagingType = create_fhir_type(
    "DeviceDefinitionPackagingType",
    "fhir.resources.devicedefinition.DeviceDefinitionPackaging",
)

DeviceDefinitionPackagingDistributorType = create_fhir_type(
    "DeviceDefinitionPackagingDistributorType",
    "fhir.resources.devicedefinition.DeviceDefinitionPackagingDistributor",
)

DeviceDefinitionPropertyType = create_fhir_type(
    "DeviceDefinitionPropertyType",
    "fhir.resources.devicedefinition.DeviceDefinitionProperty",
)

DeviceDefinitionRegulatoryIdentifierType = create_fhir_type(
    "DeviceDefinitionRegulatoryIdentifierType",
    "fhir.resources.devicedefinition.DeviceDefinitionRegulatoryIdentifier",
)

DeviceDefinitionUdiDeviceIdentifierType = create_fhir_type(
    "DeviceDefinitionUdiDeviceIdentifierType",
    "fhir.resources.devicedefinition.DeviceDefinitionUdiDeviceIdentifier",
)

DeviceDefinitionUdiDeviceIdentifierMarketDistributionType = create_fhir_type(
    "DeviceDefinitionUdiDeviceIdentifierMarketDistributionType",
    "fhir.resources.devicedefinition.DeviceDefinitionUdiDeviceIdentifierMarketDistribution",
)

DeviceDefinitionVersionType = create_fhir_type(
    "DeviceDefinitionVersionType",
    "fhir.resources.devicedefinition.DeviceDefinitionVersion",
)

DeviceDispenseType = create_fhir_type(
    "DeviceDispenseType", "fhir.resources.devicedispense.DeviceDispense"
)

DeviceDispensePerformerType = create_fhir_type(
    "DeviceDispensePerformerType",
    "fhir.resources.devicedispense.DeviceDispensePerformer",
)

DeviceMetricType = create_fhir_type(
    "DeviceMetricType", "fhir.resources.devicemetric.DeviceMetric"
)

DeviceMetricCalibrationType = create_fhir_type(
    "DeviceMetricCalibrationType", "fhir.resources.devicemetric.DeviceMetricCalibration"
)

DeviceNameType = create_fhir_type("DeviceNameType", "fhir.resources.device.DeviceName")

DevicePropertyType = create_fhir_type(
    "DevicePropertyType", "fhir.resources.device.DeviceProperty"
)

DeviceRequestType = create_fhir_type(
    "DeviceRequestType", "fhir.resources.devicerequest.DeviceRequest"
)

DeviceRequestParameterType = create_fhir_type(
    "DeviceRequestParameterType", "fhir.resources.devicerequest.DeviceRequestParameter"
)

DeviceUdiCarrierType = create_fhir_type(
    "DeviceUdiCarrierType", "fhir.resources.device.DeviceUdiCarrier"
)

DeviceUsageType = create_fhir_type(
    "DeviceUsageType", "fhir.resources.deviceusage.DeviceUsage"
)

DeviceUsageAdherenceType = create_fhir_type(
    "DeviceUsageAdherenceType", "fhir.resources.deviceusage.DeviceUsageAdherence"
)

DeviceVersionType = create_fhir_type(
    "DeviceVersionType", "fhir.resources.device.DeviceVersion"
)

DiagnosticReportType = create_fhir_type(
    "DiagnosticReportType", "fhir.resources.diagnosticreport.DiagnosticReport"
)

DiagnosticReportMediaType = create_fhir_type(
    "DiagnosticReportMediaType", "fhir.resources.diagnosticreport.DiagnosticReportMedia"
)

DiagnosticReportSupportingInfoType = create_fhir_type(
    "DiagnosticReportSupportingInfoType",
    "fhir.resources.diagnosticreport.DiagnosticReportSupportingInfo",
)

DistanceType = create_fhir_type("DistanceType", "fhir.resources.distance.Distance")

DocumentReferenceType = create_fhir_type(
    "DocumentReferenceType", "fhir.resources.documentreference.DocumentReference"
)

DocumentReferenceAttesterType = create_fhir_type(
    "DocumentReferenceAttesterType",
    "fhir.resources.documentreference.DocumentReferenceAttester",
)

DocumentReferenceContentType = create_fhir_type(
    "DocumentReferenceContentType",
    "fhir.resources.documentreference.DocumentReferenceContent",
)

DocumentReferenceContentProfileType = create_fhir_type(
    "DocumentReferenceContentProfileType",
    "fhir.resources.documentreference.DocumentReferenceContentProfile",
)

DocumentReferenceRelatesToType = create_fhir_type(
    "DocumentReferenceRelatesToType",
    "fhir.resources.documentreference.DocumentReferenceRelatesTo",
)

DomainResourceType = create_fhir_type(
    "DomainResourceType", "fhir.resources.domainresource.DomainResource"
)

DosageType = create_fhir_type("DosageType", "fhir.resources.dosage.Dosage")

DosageDoseAndRateType = create_fhir_type(
    "DosageDoseAndRateType", "fhir.resources.dosage.DosageDoseAndRate"
)

DurationType = create_fhir_type("DurationType", "fhir.resources.duration.Duration")

ElementDefinitionType = create_fhir_type(
    "ElementDefinitionType", "fhir.resources.elementdefinition.ElementDefinition"
)

ElementDefinitionBaseType = create_fhir_type(
    "ElementDefinitionBaseType",
    "fhir.resources.elementdefinition.ElementDefinitionBase",
)

ElementDefinitionBindingType = create_fhir_type(
    "ElementDefinitionBindingType",
    "fhir.resources.elementdefinition.ElementDefinitionBinding",
)

ElementDefinitionBindingAdditionalType = create_fhir_type(
    "ElementDefinitionBindingAdditionalType",
    "fhir.resources.elementdefinition.ElementDefinitionBindingAdditional",
)

ElementDefinitionConstraintType = create_fhir_type(
    "ElementDefinitionConstraintType",
    "fhir.resources.elementdefinition.ElementDefinitionConstraint",
)

ElementDefinitionExampleType = create_fhir_type(
    "ElementDefinitionExampleType",
    "fhir.resources.elementdefinition.ElementDefinitionExample",
)

ElementDefinitionMappingType = create_fhir_type(
    "ElementDefinitionMappingType",
    "fhir.resources.elementdefinition.ElementDefinitionMapping",
)

ElementDefinitionSlicingType = create_fhir_type(
    "ElementDefinitionSlicingType",
    "fhir.resources.elementdefinition.ElementDefinitionSlicing",
)

ElementDefinitionSlicingDiscriminatorType = create_fhir_type(
    "ElementDefinitionSlicingDiscriminatorType",
    "fhir.resources.elementdefinition.ElementDefinitionSlicingDiscriminator",
)

ElementDefinitionTypeType = create_fhir_type(
    "ElementDefinitionTypeType",
    "fhir.resources.elementdefinition.ElementDefinitionType",
)

EncounterType = create_fhir_type("EncounterType", "fhir.resources.encounter.Encounter")

EncounterAdmissionType = create_fhir_type(
    "EncounterAdmissionType", "fhir.resources.encounter.EncounterAdmission"
)

EncounterDiagnosisType = create_fhir_type(
    "EncounterDiagnosisType", "fhir.resources.encounter.EncounterDiagnosis"
)

EncounterHistoryType = create_fhir_type(
    "EncounterHistoryType", "fhir.resources.encounterhistory.EncounterHistory"
)

EncounterHistoryLocationType = create_fhir_type(
    "EncounterHistoryLocationType",
    "fhir.resources.encounterhistory.EncounterHistoryLocation",
)

EncounterLocationType = create_fhir_type(
    "EncounterLocationType", "fhir.resources.encounter.EncounterLocation"
)

EncounterParticipantType = create_fhir_type(
    "EncounterParticipantType", "fhir.resources.encounter.EncounterParticipant"
)

EncounterReasonType = create_fhir_type(
    "EncounterReasonType", "fhir.resources.encounter.EncounterReason"
)

EndpointType = create_fhir_type("EndpointType", "fhir.resources.endpoint.Endpoint")

EndpointPayloadType = create_fhir_type(
    "EndpointPayloadType", "fhir.resources.endpoint.EndpointPayload"
)

EnrollmentRequestType = create_fhir_type(
    "EnrollmentRequestType", "fhir.resources.enrollmentrequest.EnrollmentRequest"
)

EnrollmentResponseType = create_fhir_type(
    "EnrollmentResponseType", "fhir.resources.enrollmentresponse.EnrollmentResponse"
)

EpisodeOfCareType = create_fhir_type(
    "EpisodeOfCareType", "fhir.resources.episodeofcare.EpisodeOfCare"
)

EpisodeOfCareDiagnosisType = create_fhir_type(
    "EpisodeOfCareDiagnosisType", "fhir.resources.episodeofcare.EpisodeOfCareDiagnosis"
)

EpisodeOfCareReasonType = create_fhir_type(
    "EpisodeOfCareReasonType", "fhir.resources.episodeofcare.EpisodeOfCareReason"
)

EpisodeOfCareStatusHistoryType = create_fhir_type(
    "EpisodeOfCareStatusHistoryType",
    "fhir.resources.episodeofcare.EpisodeOfCareStatusHistory",
)

EventDefinitionType = create_fhir_type(
    "EventDefinitionType", "fhir.resources.eventdefinition.EventDefinition"
)

EvidenceType = create_fhir_type("EvidenceType", "fhir.resources.evidence.Evidence")

EvidenceCertaintyType = create_fhir_type(
    "EvidenceCertaintyType", "fhir.resources.evidence.EvidenceCertainty"
)

EvidenceReportType = create_fhir_type(
    "EvidenceReportType", "fhir.resources.evidencereport.EvidenceReport"
)

EvidenceReportRelatesToType = create_fhir_type(
    "EvidenceReportRelatesToType",
    "fhir.resources.evidencereport.EvidenceReportRelatesTo",
)

EvidenceReportRelatesToTargetType = create_fhir_type(
    "EvidenceReportRelatesToTargetType",
    "fhir.resources.evidencereport.EvidenceReportRelatesToTarget",
)

EvidenceReportSectionType = create_fhir_type(
    "EvidenceReportSectionType", "fhir.resources.evidencereport.EvidenceReportSection"
)

EvidenceReportSubjectType = create_fhir_type(
    "EvidenceReportSubjectType", "fhir.resources.evidencereport.EvidenceReportSubject"
)

EvidenceReportSubjectCharacteristicType = create_fhir_type(
    "EvidenceReportSubjectCharacteristicType",
    "fhir.resources.evidencereport.EvidenceReportSubjectCharacteristic",
)

EvidenceStatisticType = create_fhir_type(
    "EvidenceStatisticType", "fhir.resources.evidence.EvidenceStatistic"
)

EvidenceStatisticAttributeEstimateType = create_fhir_type(
    "EvidenceStatisticAttributeEstimateType",
    "fhir.resources.evidence.EvidenceStatisticAttributeEstimate",
)

EvidenceStatisticModelCharacteristicType = create_fhir_type(
    "EvidenceStatisticModelCharacteristicType",
    "fhir.resources.evidence.EvidenceStatisticModelCharacteristic",
)

EvidenceStatisticModelCharacteristicVariableType = create_fhir_type(
    "EvidenceStatisticModelCharacteristicVariableType",
    "fhir.resources.evidence.EvidenceStatisticModelCharacteristicVariable",
)

EvidenceStatisticSampleSizeType = create_fhir_type(
    "EvidenceStatisticSampleSizeType",
    "fhir.resources.evidence.EvidenceStatisticSampleSize",
)

EvidenceVariableType = create_fhir_type(
    "EvidenceVariableType", "fhir.resources.evidencevariable.EvidenceVariable"
)

EvidenceVariableCategoryType = create_fhir_type(
    "EvidenceVariableCategoryType",
    "fhir.resources.evidencevariable.EvidenceVariableCategory",
)

EvidenceVariableCharacteristicType = create_fhir_type(
    "EvidenceVariableCharacteristicType",
    "fhir.resources.evidencevariable.EvidenceVariableCharacteristic",
)

EvidenceVariableCharacteristicDefinitionByCombinationType = create_fhir_type(
    "EvidenceVariableCharacteristicDefinitionByCombinationType",
    "fhir.resources.evidencevariable.EvidenceVariableCharacteristicDefinitionByCombination",
)

EvidenceVariableCharacteristicDefinitionByTypeAndValueType = create_fhir_type(
    "EvidenceVariableCharacteristicDefinitionByTypeAndValueType",
    "fhir.resources.evidencevariable.EvidenceVariableCharacteristicDefinitionByTypeAndValue",
)

EvidenceVariableCharacteristicTimeFromEventType = create_fhir_type(
    "EvidenceVariableCharacteristicTimeFromEventType",
    "fhir.resources.evidencevariable.EvidenceVariableCharacteristicTimeFromEvent",
)

EvidenceVariableDefinitionType = create_fhir_type(
    "EvidenceVariableDefinitionType",
    "fhir.resources.evidence.EvidenceVariableDefinition",
)

ExampleScenarioType = create_fhir_type(
    "ExampleScenarioType", "fhir.resources.examplescenario.ExampleScenario"
)

ExampleScenarioActorType = create_fhir_type(
    "ExampleScenarioActorType", "fhir.resources.examplescenario.ExampleScenarioActor"
)

ExampleScenarioInstanceType = create_fhir_type(
    "ExampleScenarioInstanceType",
    "fhir.resources.examplescenario.ExampleScenarioInstance",
)

ExampleScenarioInstanceContainedInstanceType = create_fhir_type(
    "ExampleScenarioInstanceContainedInstanceType",
    "fhir.resources.examplescenario.ExampleScenarioInstanceContainedInstance",
)

ExampleScenarioInstanceVersionType = create_fhir_type(
    "ExampleScenarioInstanceVersionType",
    "fhir.resources.examplescenario.ExampleScenarioInstanceVersion",
)

ExampleScenarioProcessType = create_fhir_type(
    "ExampleScenarioProcessType",
    "fhir.resources.examplescenario.ExampleScenarioProcess",
)

ExampleScenarioProcessStepType = create_fhir_type(
    "ExampleScenarioProcessStepType",
    "fhir.resources.examplescenario.ExampleScenarioProcessStep",
)

ExampleScenarioProcessStepAlternativeType = create_fhir_type(
    "ExampleScenarioProcessStepAlternativeType",
    "fhir.resources.examplescenario.ExampleScenarioProcessStepAlternative",
)

ExampleScenarioProcessStepOperationType = create_fhir_type(
    "ExampleScenarioProcessStepOperationType",
    "fhir.resources.examplescenario.ExampleScenarioProcessStepOperation",
)

ExplanationOfBenefitType = create_fhir_type(
    "ExplanationOfBenefitType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefit",
)

ExplanationOfBenefitAccidentType = create_fhir_type(
    "ExplanationOfBenefitAccidentType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitAccident",
)

ExplanationOfBenefitAddItemType = create_fhir_type(
    "ExplanationOfBenefitAddItemType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitAddItem",
)

ExplanationOfBenefitAddItemBodySiteType = create_fhir_type(
    "ExplanationOfBenefitAddItemBodySiteType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitAddItemBodySite",
)

ExplanationOfBenefitAddItemDetailType = create_fhir_type(
    "ExplanationOfBenefitAddItemDetailType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitAddItemDetail",
)

ExplanationOfBenefitAddItemDetailSubDetailType = create_fhir_type(
    "ExplanationOfBenefitAddItemDetailSubDetailType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitAddItemDetailSubDetail",
)

ExplanationOfBenefitBenefitBalanceType = create_fhir_type(
    "ExplanationOfBenefitBenefitBalanceType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitBenefitBalance",
)

ExplanationOfBenefitBenefitBalanceFinancialType = create_fhir_type(
    "ExplanationOfBenefitBenefitBalanceFinancialType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitBenefitBalanceFinancial",
)

ExplanationOfBenefitCareTeamType = create_fhir_type(
    "ExplanationOfBenefitCareTeamType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitCareTeam",
)

ExplanationOfBenefitDiagnosisType = create_fhir_type(
    "ExplanationOfBenefitDiagnosisType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitDiagnosis",
)

ExplanationOfBenefitEventType = create_fhir_type(
    "ExplanationOfBenefitEventType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitEvent",
)

ExplanationOfBenefitInsuranceType = create_fhir_type(
    "ExplanationOfBenefitInsuranceType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitInsurance",
)

ExplanationOfBenefitItemType = create_fhir_type(
    "ExplanationOfBenefitItemType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitItem",
)

ExplanationOfBenefitItemAdjudicationType = create_fhir_type(
    "ExplanationOfBenefitItemAdjudicationType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitItemAdjudication",
)

ExplanationOfBenefitItemBodySiteType = create_fhir_type(
    "ExplanationOfBenefitItemBodySiteType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitItemBodySite",
)

ExplanationOfBenefitItemDetailType = create_fhir_type(
    "ExplanationOfBenefitItemDetailType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitItemDetail",
)

ExplanationOfBenefitItemDetailSubDetailType = create_fhir_type(
    "ExplanationOfBenefitItemDetailSubDetailType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitItemDetailSubDetail",
)

ExplanationOfBenefitItemReviewOutcomeType = create_fhir_type(
    "ExplanationOfBenefitItemReviewOutcomeType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitItemReviewOutcome",
)

ExplanationOfBenefitPayeeType = create_fhir_type(
    "ExplanationOfBenefitPayeeType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitPayee",
)

ExplanationOfBenefitPaymentType = create_fhir_type(
    "ExplanationOfBenefitPaymentType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitPayment",
)

ExplanationOfBenefitProcedureType = create_fhir_type(
    "ExplanationOfBenefitProcedureType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitProcedure",
)

ExplanationOfBenefitProcessNoteType = create_fhir_type(
    "ExplanationOfBenefitProcessNoteType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitProcessNote",
)

ExplanationOfBenefitRelatedType = create_fhir_type(
    "ExplanationOfBenefitRelatedType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitRelated",
)

ExplanationOfBenefitSupportingInfoType = create_fhir_type(
    "ExplanationOfBenefitSupportingInfoType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitSupportingInfo",
)

ExplanationOfBenefitTotalType = create_fhir_type(
    "ExplanationOfBenefitTotalType",
    "fhir.resources.explanationofbenefit.ExplanationOfBenefitTotal",
)

ExpressionType = create_fhir_type(
    "ExpressionType", "fhir.resources.expression.Expression"
)

ExtendedContactDetailType = create_fhir_type(
    "ExtendedContactDetailType",
    "fhir.resources.extendedcontactdetail.ExtendedContactDetail",
)

ExtensionType = create_fhir_type("ExtensionType", "fhir.resources.extension.Extension")

FamilyMemberHistoryType = create_fhir_type(
    "FamilyMemberHistoryType", "fhir.resources.familymemberhistory.FamilyMemberHistory"
)

FamilyMemberHistoryConditionType = create_fhir_type(
    "FamilyMemberHistoryConditionType",
    "fhir.resources.familymemberhistory.FamilyMemberHistoryCondition",
)

FamilyMemberHistoryParticipantType = create_fhir_type(
    "FamilyMemberHistoryParticipantType",
    "fhir.resources.familymemberhistory.FamilyMemberHistoryParticipant",
)

FamilyMemberHistoryProcedureType = create_fhir_type(
    "FamilyMemberHistoryProcedureType",
    "fhir.resources.familymemberhistory.FamilyMemberHistoryProcedure",
)

FlagType = create_fhir_type("FlagType", "fhir.resources.flag.Flag")

FormularyItemType = create_fhir_type(
    "FormularyItemType", "fhir.resources.formularyitem.FormularyItem"
)

GenomicStudyType = create_fhir_type(
    "GenomicStudyType", "fhir.resources.genomicstudy.GenomicStudy"
)

GenomicStudyAnalysisType = create_fhir_type(
    "GenomicStudyAnalysisType", "fhir.resources.genomicstudy.GenomicStudyAnalysis"
)

GenomicStudyAnalysisDeviceType = create_fhir_type(
    "GenomicStudyAnalysisDeviceType",
    "fhir.resources.genomicstudy.GenomicStudyAnalysisDevice",
)

GenomicStudyAnalysisInputType = create_fhir_type(
    "GenomicStudyAnalysisInputType",
    "fhir.resources.genomicstudy.GenomicStudyAnalysisInput",
)

GenomicStudyAnalysisOutputType = create_fhir_type(
    "GenomicStudyAnalysisOutputType",
    "fhir.resources.genomicstudy.GenomicStudyAnalysisOutput",
)

GenomicStudyAnalysisPerformerType = create_fhir_type(
    "GenomicStudyAnalysisPerformerType",
    "fhir.resources.genomicstudy.GenomicStudyAnalysisPerformer",
)

GoalType = create_fhir_type("GoalType", "fhir.resources.goal.Goal")

GoalTargetType = create_fhir_type("GoalTargetType", "fhir.resources.goal.GoalTarget")

GraphDefinitionType = create_fhir_type(
    "GraphDefinitionType", "fhir.resources.graphdefinition.GraphDefinition"
)

GraphDefinitionLinkType = create_fhir_type(
    "GraphDefinitionLinkType", "fhir.resources.graphdefinition.GraphDefinitionLink"
)

GraphDefinitionLinkCompartmentType = create_fhir_type(
    "GraphDefinitionLinkCompartmentType",
    "fhir.resources.graphdefinition.GraphDefinitionLinkCompartment",
)

GraphDefinitionNodeType = create_fhir_type(
    "GraphDefinitionNodeType", "fhir.resources.graphdefinition.GraphDefinitionNode"
)

GroupType = create_fhir_type("GroupType", "fhir.resources.group.Group")

GroupCharacteristicType = create_fhir_type(
    "GroupCharacteristicType", "fhir.resources.group.GroupCharacteristic"
)

GroupMemberType = create_fhir_type(
    "GroupMemberType", "fhir.resources.group.GroupMember"
)

GuidanceResponseType = create_fhir_type(
    "GuidanceResponseType", "fhir.resources.guidanceresponse.GuidanceResponse"
)

HealthcareServiceType = create_fhir_type(
    "HealthcareServiceType", "fhir.resources.healthcareservice.HealthcareService"
)

HealthcareServiceEligibilityType = create_fhir_type(
    "HealthcareServiceEligibilityType",
    "fhir.resources.healthcareservice.HealthcareServiceEligibility",
)

HumanNameType = create_fhir_type("HumanNameType", "fhir.resources.humanname.HumanName")

IdentifierType = create_fhir_type(
    "IdentifierType", "fhir.resources.identifier.Identifier"
)

ImagingSelectionType = create_fhir_type(
    "ImagingSelectionType", "fhir.resources.imagingselection.ImagingSelection"
)

ImagingSelectionInstanceType = create_fhir_type(
    "ImagingSelectionInstanceType",
    "fhir.resources.imagingselection.ImagingSelectionInstance",
)

ImagingSelectionInstanceImageRegion2DType = create_fhir_type(
    "ImagingSelectionInstanceImageRegion2DType",
    "fhir.resources.imagingselection.ImagingSelectionInstanceImageRegion2D",
)

ImagingSelectionInstanceImageRegion3DType = create_fhir_type(
    "ImagingSelectionInstanceImageRegion3DType",
    "fhir.resources.imagingselection.ImagingSelectionInstanceImageRegion3D",
)

ImagingSelectionPerformerType = create_fhir_type(
    "ImagingSelectionPerformerType",
    "fhir.resources.imagingselection.ImagingSelectionPerformer",
)

ImagingStudyType = create_fhir_type(
    "ImagingStudyType", "fhir.resources.imagingstudy.ImagingStudy"
)

ImagingStudySeriesType = create_fhir_type(
    "ImagingStudySeriesType", "fhir.resources.imagingstudy.ImagingStudySeries"
)

ImagingStudySeriesInstanceType = create_fhir_type(
    "ImagingStudySeriesInstanceType",
    "fhir.resources.imagingstudy.ImagingStudySeriesInstance",
)

ImagingStudySeriesPerformerType = create_fhir_type(
    "ImagingStudySeriesPerformerType",
    "fhir.resources.imagingstudy.ImagingStudySeriesPerformer",
)

ImmunizationType = create_fhir_type(
    "ImmunizationType", "fhir.resources.immunization.Immunization"
)

ImmunizationEvaluationType = create_fhir_type(
    "ImmunizationEvaluationType",
    "fhir.resources.immunizationevaluation.ImmunizationEvaluation",
)

ImmunizationPerformerType = create_fhir_type(
    "ImmunizationPerformerType", "fhir.resources.immunization.ImmunizationPerformer"
)

ImmunizationProgramEligibilityType = create_fhir_type(
    "ImmunizationProgramEligibilityType",
    "fhir.resources.immunization.ImmunizationProgramEligibility",
)

ImmunizationProtocolAppliedType = create_fhir_type(
    "ImmunizationProtocolAppliedType",
    "fhir.resources.immunization.ImmunizationProtocolApplied",
)

ImmunizationReactionType = create_fhir_type(
    "ImmunizationReactionType", "fhir.resources.immunization.ImmunizationReaction"
)

ImmunizationRecommendationType = create_fhir_type(
    "ImmunizationRecommendationType",
    "fhir.resources.immunizationrecommendation.ImmunizationRecommendation",
)

ImmunizationRecommendationRecommendationType = create_fhir_type(
    "ImmunizationRecommendationRecommendationType",
    "fhir.resources.immunizationrecommendation.ImmunizationRecommendationRecommendation",
)

ImmunizationRecommendationRecommendationDateCriterionType = create_fhir_type(
    "ImmunizationRecommendationRecommendationDateCriterionType",
    "fhir.resources.immunizationrecommendation.ImmunizationRecommendationRecommendationDateCriterion",
)

ImplementationGuideType = create_fhir_type(
    "ImplementationGuideType", "fhir.resources.implementationguide.ImplementationGuide"
)

ImplementationGuideDefinitionType = create_fhir_type(
    "ImplementationGuideDefinitionType",
    "fhir.resources.implementationguide.ImplementationGuideDefinition",
)

ImplementationGuideDefinitionGroupingType = create_fhir_type(
    "ImplementationGuideDefinitionGroupingType",
    "fhir.resources.implementationguide.ImplementationGuideDefinitionGrouping",
)

ImplementationGuideDefinitionPageType = create_fhir_type(
    "ImplementationGuideDefinitionPageType",
    "fhir.resources.implementationguide.ImplementationGuideDefinitionPage",
)

ImplementationGuideDefinitionParameterType = create_fhir_type(
    "ImplementationGuideDefinitionParameterType",
    "fhir.resources.implementationguide.ImplementationGuideDefinitionParameter",
)

ImplementationGuideDefinitionResourceType = create_fhir_type(
    "ImplementationGuideDefinitionResourceType",
    "fhir.resources.implementationguide.ImplementationGuideDefinitionResource",
)

ImplementationGuideDefinitionTemplateType = create_fhir_type(
    "ImplementationGuideDefinitionTemplateType",
    "fhir.resources.implementationguide.ImplementationGuideDefinitionTemplate",
)

ImplementationGuideDependsOnType = create_fhir_type(
    "ImplementationGuideDependsOnType",
    "fhir.resources.implementationguide.ImplementationGuideDependsOn",
)

ImplementationGuideGlobalType = create_fhir_type(
    "ImplementationGuideGlobalType",
    "fhir.resources.implementationguide.ImplementationGuideGlobal",
)

ImplementationGuideManifestType = create_fhir_type(
    "ImplementationGuideManifestType",
    "fhir.resources.implementationguide.ImplementationGuideManifest",
)

ImplementationGuideManifestPageType = create_fhir_type(
    "ImplementationGuideManifestPageType",
    "fhir.resources.implementationguide.ImplementationGuideManifestPage",
)

ImplementationGuideManifestResourceType = create_fhir_type(
    "ImplementationGuideManifestResourceType",
    "fhir.resources.implementationguide.ImplementationGuideManifestResource",
)

IngredientType = create_fhir_type(
    "IngredientType", "fhir.resources.ingredient.Ingredient"
)

IngredientManufacturerType = create_fhir_type(
    "IngredientManufacturerType", "fhir.resources.ingredient.IngredientManufacturer"
)

IngredientSubstanceType = create_fhir_type(
    "IngredientSubstanceType", "fhir.resources.ingredient.IngredientSubstance"
)

IngredientSubstanceStrengthType = create_fhir_type(
    "IngredientSubstanceStrengthType",
    "fhir.resources.ingredient.IngredientSubstanceStrength",
)

IngredientSubstanceStrengthReferenceStrengthType = create_fhir_type(
    "IngredientSubstanceStrengthReferenceStrengthType",
    "fhir.resources.ingredient.IngredientSubstanceStrengthReferenceStrength",
)

InsurancePlanType = create_fhir_type(
    "InsurancePlanType", "fhir.resources.insuranceplan.InsurancePlan"
)

InsurancePlanCoverageType = create_fhir_type(
    "InsurancePlanCoverageType", "fhir.resources.insuranceplan.InsurancePlanCoverage"
)

InsurancePlanCoverageBenefitType = create_fhir_type(
    "InsurancePlanCoverageBenefitType",
    "fhir.resources.insuranceplan.InsurancePlanCoverageBenefit",
)

InsurancePlanCoverageBenefitLimitType = create_fhir_type(
    "InsurancePlanCoverageBenefitLimitType",
    "fhir.resources.insuranceplan.InsurancePlanCoverageBenefitLimit",
)

InsurancePlanPlanType = create_fhir_type(
    "InsurancePlanPlanType", "fhir.resources.insuranceplan.InsurancePlanPlan"
)

InsurancePlanPlanGeneralCostType = create_fhir_type(
    "InsurancePlanPlanGeneralCostType",
    "fhir.resources.insuranceplan.InsurancePlanPlanGeneralCost",
)

InsurancePlanPlanSpecificCostType = create_fhir_type(
    "InsurancePlanPlanSpecificCostType",
    "fhir.resources.insuranceplan.InsurancePlanPlanSpecificCost",
)

InsurancePlanPlanSpecificCostBenefitType = create_fhir_type(
    "InsurancePlanPlanSpecificCostBenefitType",
    "fhir.resources.insuranceplan.InsurancePlanPlanSpecificCostBenefit",
)

InsurancePlanPlanSpecificCostBenefitCostType = create_fhir_type(
    "InsurancePlanPlanSpecificCostBenefitCostType",
    "fhir.resources.insuranceplan.InsurancePlanPlanSpecificCostBenefitCost",
)

InventoryItemType = create_fhir_type(
    "InventoryItemType", "fhir.resources.inventoryitem.InventoryItem"
)

InventoryItemAssociationType = create_fhir_type(
    "InventoryItemAssociationType",
    "fhir.resources.inventoryitem.InventoryItemAssociation",
)

InventoryItemCharacteristicType = create_fhir_type(
    "InventoryItemCharacteristicType",
    "fhir.resources.inventoryitem.InventoryItemCharacteristic",
)

InventoryItemDescriptionType = create_fhir_type(
    "InventoryItemDescriptionType",
    "fhir.resources.inventoryitem.InventoryItemDescription",
)

InventoryItemInstanceType = create_fhir_type(
    "InventoryItemInstanceType", "fhir.resources.inventoryitem.InventoryItemInstance"
)

InventoryItemNameType = create_fhir_type(
    "InventoryItemNameType", "fhir.resources.inventoryitem.InventoryItemName"
)

InventoryItemResponsibleOrganizationType = create_fhir_type(
    "InventoryItemResponsibleOrganizationType",
    "fhir.resources.inventoryitem.InventoryItemResponsibleOrganization",
)

InventoryReportType = create_fhir_type(
    "InventoryReportType", "fhir.resources.inventoryreport.InventoryReport"
)

InventoryReportInventoryListingType = create_fhir_type(
    "InventoryReportInventoryListingType",
    "fhir.resources.inventoryreport.InventoryReportInventoryListing",
)

InventoryReportInventoryListingItemType = create_fhir_type(
    "InventoryReportInventoryListingItemType",
    "fhir.resources.inventoryreport.InventoryReportInventoryListingItem",
)

InvoiceType = create_fhir_type("InvoiceType", "fhir.resources.invoice.Invoice")

InvoiceLineItemType = create_fhir_type(
    "InvoiceLineItemType", "fhir.resources.invoice.InvoiceLineItem"
)

InvoiceParticipantType = create_fhir_type(
    "InvoiceParticipantType", "fhir.resources.invoice.InvoiceParticipant"
)

LibraryType = create_fhir_type("LibraryType", "fhir.resources.library.Library")

LinkageType = create_fhir_type("LinkageType", "fhir.resources.linkage.Linkage")

LinkageItemType = create_fhir_type(
    "LinkageItemType", "fhir.resources.linkage.LinkageItem"
)

ListType = create_fhir_type("ListType", "fhir.resources.list.List")

ListEntryType = create_fhir_type("ListEntryType", "fhir.resources.list.ListEntry")

LocationType = create_fhir_type("LocationType", "fhir.resources.location.Location")

LocationPositionType = create_fhir_type(
    "LocationPositionType", "fhir.resources.location.LocationPosition"
)

ManufacturedItemDefinitionType = create_fhir_type(
    "ManufacturedItemDefinitionType",
    "fhir.resources.manufactureditemdefinition.ManufacturedItemDefinition",
)

ManufacturedItemDefinitionComponentType = create_fhir_type(
    "ManufacturedItemDefinitionComponentType",
    "fhir.resources.manufactureditemdefinition.ManufacturedItemDefinitionComponent",
)

ManufacturedItemDefinitionComponentConstituentType = create_fhir_type(
    "ManufacturedItemDefinitionComponentConstituentType",
    "fhir.resources.manufactureditemdefinition.ManufacturedItemDefinitionComponentConstituent",
)

ManufacturedItemDefinitionPropertyType = create_fhir_type(
    "ManufacturedItemDefinitionPropertyType",
    "fhir.resources.manufactureditemdefinition.ManufacturedItemDefinitionProperty",
)

MarketingStatusType = create_fhir_type(
    "MarketingStatusType", "fhir.resources.marketingstatus.MarketingStatus"
)

MeasureType = create_fhir_type("MeasureType", "fhir.resources.measure.Measure")

MeasureGroupType = create_fhir_type(
    "MeasureGroupType", "fhir.resources.measure.MeasureGroup"
)

MeasureGroupPopulationType = create_fhir_type(
    "MeasureGroupPopulationType", "fhir.resources.measure.MeasureGroupPopulation"
)

MeasureGroupStratifierType = create_fhir_type(
    "MeasureGroupStratifierType", "fhir.resources.measure.MeasureGroupStratifier"
)

MeasureGroupStratifierComponentType = create_fhir_type(
    "MeasureGroupStratifierComponentType",
    "fhir.resources.measure.MeasureGroupStratifierComponent",
)

MeasureReportType = create_fhir_type(
    "MeasureReportType", "fhir.resources.measurereport.MeasureReport"
)

MeasureReportGroupType = create_fhir_type(
    "MeasureReportGroupType", "fhir.resources.measurereport.MeasureReportGroup"
)

MeasureReportGroupPopulationType = create_fhir_type(
    "MeasureReportGroupPopulationType",
    "fhir.resources.measurereport.MeasureReportGroupPopulation",
)

MeasureReportGroupStratifierType = create_fhir_type(
    "MeasureReportGroupStratifierType",
    "fhir.resources.measurereport.MeasureReportGroupStratifier",
)

MeasureReportGroupStratifierStratumType = create_fhir_type(
    "MeasureReportGroupStratifierStratumType",
    "fhir.resources.measurereport.MeasureReportGroupStratifierStratum",
)

MeasureReportGroupStratifierStratumComponentType = create_fhir_type(
    "MeasureReportGroupStratifierStratumComponentType",
    "fhir.resources.measurereport.MeasureReportGroupStratifierStratumComponent",
)

MeasureReportGroupStratifierStratumPopulationType = create_fhir_type(
    "MeasureReportGroupStratifierStratumPopulationType",
    "fhir.resources.measurereport.MeasureReportGroupStratifierStratumPopulation",
)

MeasureSupplementalDataType = create_fhir_type(
    "MeasureSupplementalDataType", "fhir.resources.measure.MeasureSupplementalData"
)

MeasureTermType = create_fhir_type(
    "MeasureTermType", "fhir.resources.measure.MeasureTerm"
)

MedicationType = create_fhir_type(
    "MedicationType", "fhir.resources.medication.Medication"
)

MedicationAdministrationType = create_fhir_type(
    "MedicationAdministrationType",
    "fhir.resources.medicationadministration.MedicationAdministration",
)

MedicationAdministrationDosageType = create_fhir_type(
    "MedicationAdministrationDosageType",
    "fhir.resources.medicationadministration.MedicationAdministrationDosage",
)

MedicationAdministrationPerformerType = create_fhir_type(
    "MedicationAdministrationPerformerType",
    "fhir.resources.medicationadministration.MedicationAdministrationPerformer",
)

MedicationBatchType = create_fhir_type(
    "MedicationBatchType", "fhir.resources.medication.MedicationBatch"
)

MedicationDispenseType = create_fhir_type(
    "MedicationDispenseType", "fhir.resources.medicationdispense.MedicationDispense"
)

MedicationDispensePerformerType = create_fhir_type(
    "MedicationDispensePerformerType",
    "fhir.resources.medicationdispense.MedicationDispensePerformer",
)

MedicationDispenseSubstitutionType = create_fhir_type(
    "MedicationDispenseSubstitutionType",
    "fhir.resources.medicationdispense.MedicationDispenseSubstitution",
)

MedicationIngredientType = create_fhir_type(
    "MedicationIngredientType", "fhir.resources.medication.MedicationIngredient"
)

MedicationKnowledgeType = create_fhir_type(
    "MedicationKnowledgeType", "fhir.resources.medicationknowledge.MedicationKnowledge"
)

MedicationKnowledgeCostType = create_fhir_type(
    "MedicationKnowledgeCostType",
    "fhir.resources.medicationknowledge.MedicationKnowledgeCost",
)

MedicationKnowledgeDefinitionalType = create_fhir_type(
    "MedicationKnowledgeDefinitionalType",
    "fhir.resources.medicationknowledge.MedicationKnowledgeDefinitional",
)

MedicationKnowledgeDefinitionalDrugCharacteristicType = create_fhir_type(
    "MedicationKnowledgeDefinitionalDrugCharacteristicType",
    "fhir.resources.medicationknowledge.MedicationKnowledgeDefinitionalDrugCharacteristic",
)

MedicationKnowledgeDefinitionalIngredientType = create_fhir_type(
    "MedicationKnowledgeDefinitionalIngredientType",
    "fhir.resources.medicationknowledge.MedicationKnowledgeDefinitionalIngredient",
)

MedicationKnowledgeIndicationGuidelineType = create_fhir_type(
    "MedicationKnowledgeIndicationGuidelineType",
    "fhir.resources.medicationknowledge.MedicationKnowledgeIndicationGuideline",
)

MedicationKnowledgeIndicationGuidelineDosingGuidelineType = create_fhir_type(
    "MedicationKnowledgeIndicationGuidelineDosingGuidelineType",
    "fhir.resources.medicationknowledge.MedicationKnowledgeIndicationGuidelineDosingGuideline",
)

MedicationKnowledgeIndicationGuidelineDosingGuidelineDosageType = create_fhir_type(
    "MedicationKnowledgeIndicationGuidelineDosingGuidelineDosageType",
    "fhir.resources.medicationknowledge.MedicationKnowledgeIndicationGuidelineDosingGuidelineDosage",
)

MedicationKnowledgeIndicationGuidelineDosingGuidelinePatientCharacteristicType = create_fhir_type(
    "MedicationKnowledgeIndicationGuidelineDosingGuidelinePatientCharacteristicType",
    "fhir.resources.medicationknowledge.MedicationKnowledgeIndicationGuidelineDosingGuidelinePatientCharacteristic",
)

MedicationKnowledgeMedicineClassificationType = create_fhir_type(
    "MedicationKnowledgeMedicineClassificationType",
    "fhir.resources.medicationknowledge.MedicationKnowledgeMedicineClassification",
)

MedicationKnowledgeMonitoringProgramType = create_fhir_type(
    "MedicationKnowledgeMonitoringProgramType",
    "fhir.resources.medicationknowledge.MedicationKnowledgeMonitoringProgram",
)

MedicationKnowledgeMonographType = create_fhir_type(
    "MedicationKnowledgeMonographType",
    "fhir.resources.medicationknowledge.MedicationKnowledgeMonograph",
)

MedicationKnowledgePackagingType = create_fhir_type(
    "MedicationKnowledgePackagingType",
    "fhir.resources.medicationknowledge.MedicationKnowledgePackaging",
)

MedicationKnowledgeRegulatoryType = create_fhir_type(
    "MedicationKnowledgeRegulatoryType",
    "fhir.resources.medicationknowledge.MedicationKnowledgeRegulatory",
)

MedicationKnowledgeRegulatoryMaxDispenseType = create_fhir_type(
    "MedicationKnowledgeRegulatoryMaxDispenseType",
    "fhir.resources.medicationknowledge.MedicationKnowledgeRegulatoryMaxDispense",
)

MedicationKnowledgeRegulatorySubstitutionType = create_fhir_type(
    "MedicationKnowledgeRegulatorySubstitutionType",
    "fhir.resources.medicationknowledge.MedicationKnowledgeRegulatorySubstitution",
)

MedicationKnowledgeRelatedMedicationKnowledgeType = create_fhir_type(
    "MedicationKnowledgeRelatedMedicationKnowledgeType",
    "fhir.resources.medicationknowledge.MedicationKnowledgeRelatedMedicationKnowledge",
)

MedicationKnowledgeStorageGuidelineType = create_fhir_type(
    "MedicationKnowledgeStorageGuidelineType",
    "fhir.resources.medicationknowledge.MedicationKnowledgeStorageGuideline",
)

MedicationKnowledgeStorageGuidelineEnvironmentalSettingType = create_fhir_type(
    "MedicationKnowledgeStorageGuidelineEnvironmentalSettingType",
    "fhir.resources.medicationknowledge.MedicationKnowledgeStorageGuidelineEnvironmentalSetting",
)

MedicationRequestType = create_fhir_type(
    "MedicationRequestType", "fhir.resources.medicationrequest.MedicationRequest"
)

MedicationRequestDispenseRequestType = create_fhir_type(
    "MedicationRequestDispenseRequestType",
    "fhir.resources.medicationrequest.MedicationRequestDispenseRequest",
)

MedicationRequestDispenseRequestInitialFillType = create_fhir_type(
    "MedicationRequestDispenseRequestInitialFillType",
    "fhir.resources.medicationrequest.MedicationRequestDispenseRequestInitialFill",
)

MedicationRequestSubstitutionType = create_fhir_type(
    "MedicationRequestSubstitutionType",
    "fhir.resources.medicationrequest.MedicationRequestSubstitution",
)

MedicationStatementType = create_fhir_type(
    "MedicationStatementType", "fhir.resources.medicationstatement.MedicationStatement"
)

MedicationStatementAdherenceType = create_fhir_type(
    "MedicationStatementAdherenceType",
    "fhir.resources.medicationstatement.MedicationStatementAdherence",
)

MedicinalProductDefinitionType = create_fhir_type(
    "MedicinalProductDefinitionType",
    "fhir.resources.medicinalproductdefinition.MedicinalProductDefinition",
)

MedicinalProductDefinitionCharacteristicType = create_fhir_type(
    "MedicinalProductDefinitionCharacteristicType",
    "fhir.resources.medicinalproductdefinition.MedicinalProductDefinitionCharacteristic",
)

MedicinalProductDefinitionContactType = create_fhir_type(
    "MedicinalProductDefinitionContactType",
    "fhir.resources.medicinalproductdefinition.MedicinalProductDefinitionContact",
)

MedicinalProductDefinitionCrossReferenceType = create_fhir_type(
    "MedicinalProductDefinitionCrossReferenceType",
    "fhir.resources.medicinalproductdefinition.MedicinalProductDefinitionCrossReference",
)

MedicinalProductDefinitionNameType = create_fhir_type(
    "MedicinalProductDefinitionNameType",
    "fhir.resources.medicinalproductdefinition.MedicinalProductDefinitionName",
)

MedicinalProductDefinitionNamePartType = create_fhir_type(
    "MedicinalProductDefinitionNamePartType",
    "fhir.resources.medicinalproductdefinition.MedicinalProductDefinitionNamePart",
)

MedicinalProductDefinitionNameUsageType = create_fhir_type(
    "MedicinalProductDefinitionNameUsageType",
    "fhir.resources.medicinalproductdefinition.MedicinalProductDefinitionNameUsage",
)

MedicinalProductDefinitionOperationType = create_fhir_type(
    "MedicinalProductDefinitionOperationType",
    "fhir.resources.medicinalproductdefinition.MedicinalProductDefinitionOperation",
)

MessageDefinitionType = create_fhir_type(
    "MessageDefinitionType", "fhir.resources.messagedefinition.MessageDefinition"
)

MessageDefinitionAllowedResponseType = create_fhir_type(
    "MessageDefinitionAllowedResponseType",
    "fhir.resources.messagedefinition.MessageDefinitionAllowedResponse",
)

MessageDefinitionFocusType = create_fhir_type(
    "MessageDefinitionFocusType",
    "fhir.resources.messagedefinition.MessageDefinitionFocus",
)

MessageHeaderType = create_fhir_type(
    "MessageHeaderType", "fhir.resources.messageheader.MessageHeader"
)

MessageHeaderDestinationType = create_fhir_type(
    "MessageHeaderDestinationType",
    "fhir.resources.messageheader.MessageHeaderDestination",
)

MessageHeaderResponseType = create_fhir_type(
    "MessageHeaderResponseType", "fhir.resources.messageheader.MessageHeaderResponse"
)

MessageHeaderSourceType = create_fhir_type(
    "MessageHeaderSourceType", "fhir.resources.messageheader.MessageHeaderSource"
)

MetaType = create_fhir_type("MetaType", "fhir.resources.meta.Meta")

MetadataResourceType = create_fhir_type(
    "MetadataResourceType", "fhir.resources.metadataresource.MetadataResource"
)

MolecularSequenceType = create_fhir_type(
    "MolecularSequenceType", "fhir.resources.molecularsequence.MolecularSequence"
)

MolecularSequenceRelativeType = create_fhir_type(
    "MolecularSequenceRelativeType",
    "fhir.resources.molecularsequence.MolecularSequenceRelative",
)

MolecularSequenceRelativeEditType = create_fhir_type(
    "MolecularSequenceRelativeEditType",
    "fhir.resources.molecularsequence.MolecularSequenceRelativeEdit",
)

MolecularSequenceRelativeStartingSequenceType = create_fhir_type(
    "MolecularSequenceRelativeStartingSequenceType",
    "fhir.resources.molecularsequence.MolecularSequenceRelativeStartingSequence",
)

MonetaryComponentType = create_fhir_type(
    "MonetaryComponentType", "fhir.resources.monetarycomponent.MonetaryComponent"
)

MoneyType = create_fhir_type("MoneyType", "fhir.resources.money.Money")

NamingSystemType = create_fhir_type(
    "NamingSystemType", "fhir.resources.namingsystem.NamingSystem"
)

NamingSystemUniqueIdType = create_fhir_type(
    "NamingSystemUniqueIdType", "fhir.resources.namingsystem.NamingSystemUniqueId"
)

NarrativeType = create_fhir_type("NarrativeType", "fhir.resources.narrative.Narrative")

NutritionIntakeType = create_fhir_type(
    "NutritionIntakeType", "fhir.resources.nutritionintake.NutritionIntake"
)

NutritionIntakeConsumedItemType = create_fhir_type(
    "NutritionIntakeConsumedItemType",
    "fhir.resources.nutritionintake.NutritionIntakeConsumedItem",
)

NutritionIntakeIngredientLabelType = create_fhir_type(
    "NutritionIntakeIngredientLabelType",
    "fhir.resources.nutritionintake.NutritionIntakeIngredientLabel",
)

NutritionIntakePerformerType = create_fhir_type(
    "NutritionIntakePerformerType",
    "fhir.resources.nutritionintake.NutritionIntakePerformer",
)

NutritionOrderType = create_fhir_type(
    "NutritionOrderType", "fhir.resources.nutritionorder.NutritionOrder"
)

NutritionOrderEnteralFormulaType = create_fhir_type(
    "NutritionOrderEnteralFormulaType",
    "fhir.resources.nutritionorder.NutritionOrderEnteralFormula",
)

NutritionOrderEnteralFormulaAdditiveType = create_fhir_type(
    "NutritionOrderEnteralFormulaAdditiveType",
    "fhir.resources.nutritionorder.NutritionOrderEnteralFormulaAdditive",
)

NutritionOrderEnteralFormulaAdministrationType = create_fhir_type(
    "NutritionOrderEnteralFormulaAdministrationType",
    "fhir.resources.nutritionorder.NutritionOrderEnteralFormulaAdministration",
)

NutritionOrderEnteralFormulaAdministrationScheduleType = create_fhir_type(
    "NutritionOrderEnteralFormulaAdministrationScheduleType",
    "fhir.resources.nutritionorder.NutritionOrderEnteralFormulaAdministrationSchedule",
)

NutritionOrderOralDietType = create_fhir_type(
    "NutritionOrderOralDietType", "fhir.resources.nutritionorder.NutritionOrderOralDiet"
)

NutritionOrderOralDietNutrientType = create_fhir_type(
    "NutritionOrderOralDietNutrientType",
    "fhir.resources.nutritionorder.NutritionOrderOralDietNutrient",
)

NutritionOrderOralDietScheduleType = create_fhir_type(
    "NutritionOrderOralDietScheduleType",
    "fhir.resources.nutritionorder.NutritionOrderOralDietSchedule",
)

NutritionOrderOralDietTextureType = create_fhir_type(
    "NutritionOrderOralDietTextureType",
    "fhir.resources.nutritionorder.NutritionOrderOralDietTexture",
)

NutritionOrderSupplementType = create_fhir_type(
    "NutritionOrderSupplementType",
    "fhir.resources.nutritionorder.NutritionOrderSupplement",
)

NutritionOrderSupplementScheduleType = create_fhir_type(
    "NutritionOrderSupplementScheduleType",
    "fhir.resources.nutritionorder.NutritionOrderSupplementSchedule",
)

NutritionProductType = create_fhir_type(
    "NutritionProductType", "fhir.resources.nutritionproduct.NutritionProduct"
)

NutritionProductCharacteristicType = create_fhir_type(
    "NutritionProductCharacteristicType",
    "fhir.resources.nutritionproduct.NutritionProductCharacteristic",
)

NutritionProductIngredientType = create_fhir_type(
    "NutritionProductIngredientType",
    "fhir.resources.nutritionproduct.NutritionProductIngredient",
)

NutritionProductInstanceType = create_fhir_type(
    "NutritionProductInstanceType",
    "fhir.resources.nutritionproduct.NutritionProductInstance",
)

NutritionProductNutrientType = create_fhir_type(
    "NutritionProductNutrientType",
    "fhir.resources.nutritionproduct.NutritionProductNutrient",
)

ObservationType = create_fhir_type(
    "ObservationType", "fhir.resources.observation.Observation"
)

ObservationComponentType = create_fhir_type(
    "ObservationComponentType", "fhir.resources.observation.ObservationComponent"
)

ObservationDefinitionType = create_fhir_type(
    "ObservationDefinitionType",
    "fhir.resources.observationdefinition.ObservationDefinition",
)

ObservationDefinitionComponentType = create_fhir_type(
    "ObservationDefinitionComponentType",
    "fhir.resources.observationdefinition.ObservationDefinitionComponent",
)

ObservationDefinitionQualifiedValueType = create_fhir_type(
    "ObservationDefinitionQualifiedValueType",
    "fhir.resources.observationdefinition.ObservationDefinitionQualifiedValue",
)

ObservationReferenceRangeType = create_fhir_type(
    "ObservationReferenceRangeType",
    "fhir.resources.observation.ObservationReferenceRange",
)

ObservationTriggeredByType = create_fhir_type(
    "ObservationTriggeredByType", "fhir.resources.observation.ObservationTriggeredBy"
)

OperationDefinitionType = create_fhir_type(
    "OperationDefinitionType", "fhir.resources.operationdefinition.OperationDefinition"
)

OperationDefinitionOverloadType = create_fhir_type(
    "OperationDefinitionOverloadType",
    "fhir.resources.operationdefinition.OperationDefinitionOverload",
)

OperationDefinitionParameterType = create_fhir_type(
    "OperationDefinitionParameterType",
    "fhir.resources.operationdefinition.OperationDefinitionParameter",
)

OperationDefinitionParameterBindingType = create_fhir_type(
    "OperationDefinitionParameterBindingType",
    "fhir.resources.operationdefinition.OperationDefinitionParameterBinding",
)

OperationDefinitionParameterReferencedFromType = create_fhir_type(
    "OperationDefinitionParameterReferencedFromType",
    "fhir.resources.operationdefinition.OperationDefinitionParameterReferencedFrom",
)

OperationOutcomeType = create_fhir_type(
    "OperationOutcomeType", "fhir.resources.operationoutcome.OperationOutcome"
)

OperationOutcomeIssueType = create_fhir_type(
    "OperationOutcomeIssueType", "fhir.resources.operationoutcome.OperationOutcomeIssue"
)

OrganizationType = create_fhir_type(
    "OrganizationType", "fhir.resources.organization.Organization"
)

OrganizationAffiliationType = create_fhir_type(
    "OrganizationAffiliationType",
    "fhir.resources.organizationaffiliation.OrganizationAffiliation",
)

OrganizationQualificationType = create_fhir_type(
    "OrganizationQualificationType",
    "fhir.resources.organization.OrganizationQualification",
)

PackagedProductDefinitionType = create_fhir_type(
    "PackagedProductDefinitionType",
    "fhir.resources.packagedproductdefinition.PackagedProductDefinition",
)

PackagedProductDefinitionLegalStatusOfSupplyType = create_fhir_type(
    "PackagedProductDefinitionLegalStatusOfSupplyType",
    "fhir.resources.packagedproductdefinition.PackagedProductDefinitionLegalStatusOfSupply",
)

PackagedProductDefinitionPackagingType = create_fhir_type(
    "PackagedProductDefinitionPackagingType",
    "fhir.resources.packagedproductdefinition.PackagedProductDefinitionPackaging",
)

PackagedProductDefinitionPackagingContainedItemType = create_fhir_type(
    "PackagedProductDefinitionPackagingContainedItemType",
    "fhir.resources.packagedproductdefinition.PackagedProductDefinitionPackagingContainedItem",
)

PackagedProductDefinitionPackagingPropertyType = create_fhir_type(
    "PackagedProductDefinitionPackagingPropertyType",
    "fhir.resources.packagedproductdefinition.PackagedProductDefinitionPackagingProperty",
)

ParameterDefinitionType = create_fhir_type(
    "ParameterDefinitionType", "fhir.resources.parameterdefinition.ParameterDefinition"
)

ParametersType = create_fhir_type(
    "ParametersType", "fhir.resources.parameters.Parameters"
)

ParametersParameterType = create_fhir_type(
    "ParametersParameterType", "fhir.resources.parameters.ParametersParameter"
)

PatientType = create_fhir_type("PatientType", "fhir.resources.patient.Patient")

PatientCommunicationType = create_fhir_type(
    "PatientCommunicationType", "fhir.resources.patient.PatientCommunication"
)

PatientContactType = create_fhir_type(
    "PatientContactType", "fhir.resources.patient.PatientContact"
)

PatientLinkType = create_fhir_type(
    "PatientLinkType", "fhir.resources.patient.PatientLink"
)

PaymentNoticeType = create_fhir_type(
    "PaymentNoticeType", "fhir.resources.paymentnotice.PaymentNotice"
)

PaymentReconciliationType = create_fhir_type(
    "PaymentReconciliationType",
    "fhir.resources.paymentreconciliation.PaymentReconciliation",
)

PaymentReconciliationAllocationType = create_fhir_type(
    "PaymentReconciliationAllocationType",
    "fhir.resources.paymentreconciliation.PaymentReconciliationAllocation",
)

PaymentReconciliationProcessNoteType = create_fhir_type(
    "PaymentReconciliationProcessNoteType",
    "fhir.resources.paymentreconciliation.PaymentReconciliationProcessNote",
)

PeriodType = create_fhir_type("PeriodType", "fhir.resources.period.Period")

PermissionType = create_fhir_type(
    "PermissionType", "fhir.resources.permission.Permission"
)

PermissionJustificationType = create_fhir_type(
    "PermissionJustificationType", "fhir.resources.permission.PermissionJustification"
)

PermissionRuleType = create_fhir_type(
    "PermissionRuleType", "fhir.resources.permission.PermissionRule"
)

PermissionRuleActivityType = create_fhir_type(
    "PermissionRuleActivityType", "fhir.resources.permission.PermissionRuleActivity"
)

PermissionRuleDataType = create_fhir_type(
    "PermissionRuleDataType", "fhir.resources.permission.PermissionRuleData"
)

PermissionRuleDataResourceType = create_fhir_type(
    "PermissionRuleDataResourceType",
    "fhir.resources.permission.PermissionRuleDataResource",
)

PersonType = create_fhir_type("PersonType", "fhir.resources.person.Person")

PersonCommunicationType = create_fhir_type(
    "PersonCommunicationType", "fhir.resources.person.PersonCommunication"
)

PersonLinkType = create_fhir_type("PersonLinkType", "fhir.resources.person.PersonLink")

PlanDefinitionType = create_fhir_type(
    "PlanDefinitionType", "fhir.resources.plandefinition.PlanDefinition"
)

PlanDefinitionActionType = create_fhir_type(
    "PlanDefinitionActionType", "fhir.resources.plandefinition.PlanDefinitionAction"
)

PlanDefinitionActionConditionType = create_fhir_type(
    "PlanDefinitionActionConditionType",
    "fhir.resources.plandefinition.PlanDefinitionActionCondition",
)

PlanDefinitionActionDynamicValueType = create_fhir_type(
    "PlanDefinitionActionDynamicValueType",
    "fhir.resources.plandefinition.PlanDefinitionActionDynamicValue",
)

PlanDefinitionActionInputType = create_fhir_type(
    "PlanDefinitionActionInputType",
    "fhir.resources.plandefinition.PlanDefinitionActionInput",
)

PlanDefinitionActionOutputType = create_fhir_type(
    "PlanDefinitionActionOutputType",
    "fhir.resources.plandefinition.PlanDefinitionActionOutput",
)

PlanDefinitionActionParticipantType = create_fhir_type(
    "PlanDefinitionActionParticipantType",
    "fhir.resources.plandefinition.PlanDefinitionActionParticipant",
)

PlanDefinitionActionRelatedActionType = create_fhir_type(
    "PlanDefinitionActionRelatedActionType",
    "fhir.resources.plandefinition.PlanDefinitionActionRelatedAction",
)

PlanDefinitionActorType = create_fhir_type(
    "PlanDefinitionActorType", "fhir.resources.plandefinition.PlanDefinitionActor"
)

PlanDefinitionActorOptionType = create_fhir_type(
    "PlanDefinitionActorOptionType",
    "fhir.resources.plandefinition.PlanDefinitionActorOption",
)

PlanDefinitionGoalType = create_fhir_type(
    "PlanDefinitionGoalType", "fhir.resources.plandefinition.PlanDefinitionGoal"
)

PlanDefinitionGoalTargetType = create_fhir_type(
    "PlanDefinitionGoalTargetType",
    "fhir.resources.plandefinition.PlanDefinitionGoalTarget",
)

PractitionerType = create_fhir_type(
    "PractitionerType", "fhir.resources.practitioner.Practitioner"
)

PractitionerCommunicationType = create_fhir_type(
    "PractitionerCommunicationType",
    "fhir.resources.practitioner.PractitionerCommunication",
)

PractitionerQualificationType = create_fhir_type(
    "PractitionerQualificationType",
    "fhir.resources.practitioner.PractitionerQualification",
)

PractitionerRoleType = create_fhir_type(
    "PractitionerRoleType", "fhir.resources.practitionerrole.PractitionerRole"
)

PrimitiveTypeType = create_fhir_type(
    "PrimitiveTypeType", "fhir.resources.primitivetype.PrimitiveType"
)

ProcedureType = create_fhir_type("ProcedureType", "fhir.resources.procedure.Procedure")

ProcedureFocalDeviceType = create_fhir_type(
    "ProcedureFocalDeviceType", "fhir.resources.procedure.ProcedureFocalDevice"
)

ProcedurePerformerType = create_fhir_type(
    "ProcedurePerformerType", "fhir.resources.procedure.ProcedurePerformer"
)

ProductShelfLifeType = create_fhir_type(
    "ProductShelfLifeType", "fhir.resources.productshelflife.ProductShelfLife"
)

ProvenanceType = create_fhir_type(
    "ProvenanceType", "fhir.resources.provenance.Provenance"
)

ProvenanceAgentType = create_fhir_type(
    "ProvenanceAgentType", "fhir.resources.provenance.ProvenanceAgent"
)

ProvenanceEntityType = create_fhir_type(
    "ProvenanceEntityType", "fhir.resources.provenance.ProvenanceEntity"
)

QuantityType = create_fhir_type("QuantityType", "fhir.resources.quantity.Quantity")

QuestionnaireType = create_fhir_type(
    "QuestionnaireType", "fhir.resources.questionnaire.Questionnaire"
)

QuestionnaireItemType = create_fhir_type(
    "QuestionnaireItemType", "fhir.resources.questionnaire.QuestionnaireItem"
)

QuestionnaireItemAnswerOptionType = create_fhir_type(
    "QuestionnaireItemAnswerOptionType",
    "fhir.resources.questionnaire.QuestionnaireItemAnswerOption",
)

QuestionnaireItemEnableWhenType = create_fhir_type(
    "QuestionnaireItemEnableWhenType",
    "fhir.resources.questionnaire.QuestionnaireItemEnableWhen",
)

QuestionnaireItemInitialType = create_fhir_type(
    "QuestionnaireItemInitialType",
    "fhir.resources.questionnaire.QuestionnaireItemInitial",
)

QuestionnaireResponseType = create_fhir_type(
    "QuestionnaireResponseType",
    "fhir.resources.questionnaireresponse.QuestionnaireResponse",
)

QuestionnaireResponseItemType = create_fhir_type(
    "QuestionnaireResponseItemType",
    "fhir.resources.questionnaireresponse.QuestionnaireResponseItem",
)

QuestionnaireResponseItemAnswerType = create_fhir_type(
    "QuestionnaireResponseItemAnswerType",
    "fhir.resources.questionnaireresponse.QuestionnaireResponseItemAnswer",
)

RangeType = create_fhir_type("RangeType", "fhir.resources.range.Range")

RatioType = create_fhir_type("RatioType", "fhir.resources.ratio.Ratio")

RatioRangeType = create_fhir_type(
    "RatioRangeType", "fhir.resources.ratiorange.RatioRange"
)

ReferenceType = create_fhir_type("ReferenceType", "fhir.resources.reference.Reference")

RegulatedAuthorizationType = create_fhir_type(
    "RegulatedAuthorizationType",
    "fhir.resources.regulatedauthorization.RegulatedAuthorization",
)

RegulatedAuthorizationCaseType = create_fhir_type(
    "RegulatedAuthorizationCaseType",
    "fhir.resources.regulatedauthorization.RegulatedAuthorizationCase",
)

RelatedArtifactType = create_fhir_type(
    "RelatedArtifactType", "fhir.resources.relatedartifact.RelatedArtifact"
)

RelatedPersonType = create_fhir_type(
    "RelatedPersonType", "fhir.resources.relatedperson.RelatedPerson"
)

RelatedPersonCommunicationType = create_fhir_type(
    "RelatedPersonCommunicationType",
    "fhir.resources.relatedperson.RelatedPersonCommunication",
)

RequestOrchestrationType = create_fhir_type(
    "RequestOrchestrationType",
    "fhir.resources.requestorchestration.RequestOrchestration",
)

RequestOrchestrationActionType = create_fhir_type(
    "RequestOrchestrationActionType",
    "fhir.resources.requestorchestration.RequestOrchestrationAction",
)

RequestOrchestrationActionConditionType = create_fhir_type(
    "RequestOrchestrationActionConditionType",
    "fhir.resources.requestorchestration.RequestOrchestrationActionCondition",
)

RequestOrchestrationActionDynamicValueType = create_fhir_type(
    "RequestOrchestrationActionDynamicValueType",
    "fhir.resources.requestorchestration.RequestOrchestrationActionDynamicValue",
)

RequestOrchestrationActionInputType = create_fhir_type(
    "RequestOrchestrationActionInputType",
    "fhir.resources.requestorchestration.RequestOrchestrationActionInput",
)

RequestOrchestrationActionOutputType = create_fhir_type(
    "RequestOrchestrationActionOutputType",
    "fhir.resources.requestorchestration.RequestOrchestrationActionOutput",
)

RequestOrchestrationActionParticipantType = create_fhir_type(
    "RequestOrchestrationActionParticipantType",
    "fhir.resources.requestorchestration.RequestOrchestrationActionParticipant",
)

RequestOrchestrationActionRelatedActionType = create_fhir_type(
    "RequestOrchestrationActionRelatedActionType",
    "fhir.resources.requestorchestration.RequestOrchestrationActionRelatedAction",
)

RequirementsType = create_fhir_type(
    "RequirementsType", "fhir.resources.requirements.Requirements"
)

RequirementsStatementType = create_fhir_type(
    "RequirementsStatementType", "fhir.resources.requirements.RequirementsStatement"
)

ResearchStudyType = create_fhir_type(
    "ResearchStudyType", "fhir.resources.researchstudy.ResearchStudy"
)

ResearchStudyAssociatedPartyType = create_fhir_type(
    "ResearchStudyAssociatedPartyType",
    "fhir.resources.researchstudy.ResearchStudyAssociatedParty",
)

ResearchStudyComparisonGroupType = create_fhir_type(
    "ResearchStudyComparisonGroupType",
    "fhir.resources.researchstudy.ResearchStudyComparisonGroup",
)

ResearchStudyLabelType = create_fhir_type(
    "ResearchStudyLabelType", "fhir.resources.researchstudy.ResearchStudyLabel"
)

ResearchStudyObjectiveType = create_fhir_type(
    "ResearchStudyObjectiveType", "fhir.resources.researchstudy.ResearchStudyObjective"
)

ResearchStudyOutcomeMeasureType = create_fhir_type(
    "ResearchStudyOutcomeMeasureType",
    "fhir.resources.researchstudy.ResearchStudyOutcomeMeasure",
)

ResearchStudyProgressStatusType = create_fhir_type(
    "ResearchStudyProgressStatusType",
    "fhir.resources.researchstudy.ResearchStudyProgressStatus",
)

ResearchStudyRecruitmentType = create_fhir_type(
    "ResearchStudyRecruitmentType",
    "fhir.resources.researchstudy.ResearchStudyRecruitment",
)

ResearchSubjectType = create_fhir_type(
    "ResearchSubjectType", "fhir.resources.researchsubject.ResearchSubject"
)

ResearchSubjectProgressType = create_fhir_type(
    "ResearchSubjectProgressType",
    "fhir.resources.researchsubject.ResearchSubjectProgress",
)

RiskAssessmentType = create_fhir_type(
    "RiskAssessmentType", "fhir.resources.riskassessment.RiskAssessment"
)

RiskAssessmentPredictionType = create_fhir_type(
    "RiskAssessmentPredictionType",
    "fhir.resources.riskassessment.RiskAssessmentPrediction",
)

SampledDataType = create_fhir_type(
    "SampledDataType", "fhir.resources.sampleddata.SampledData"
)

ScheduleType = create_fhir_type("ScheduleType", "fhir.resources.schedule.Schedule")

SearchParameterType = create_fhir_type(
    "SearchParameterType", "fhir.resources.searchparameter.SearchParameter"
)

SearchParameterComponentType = create_fhir_type(
    "SearchParameterComponentType",
    "fhir.resources.searchparameter.SearchParameterComponent",
)

ServiceRequestType = create_fhir_type(
    "ServiceRequestType", "fhir.resources.servicerequest.ServiceRequest"
)

ServiceRequestOrderDetailType = create_fhir_type(
    "ServiceRequestOrderDetailType",
    "fhir.resources.servicerequest.ServiceRequestOrderDetail",
)

ServiceRequestOrderDetailParameterType = create_fhir_type(
    "ServiceRequestOrderDetailParameterType",
    "fhir.resources.servicerequest.ServiceRequestOrderDetailParameter",
)

ServiceRequestPatientInstructionType = create_fhir_type(
    "ServiceRequestPatientInstructionType",
    "fhir.resources.servicerequest.ServiceRequestPatientInstruction",
)

SignatureType = create_fhir_type("SignatureType", "fhir.resources.signature.Signature")

SlotType = create_fhir_type("SlotType", "fhir.resources.slot.Slot")

SpecimenType = create_fhir_type("SpecimenType", "fhir.resources.specimen.Specimen")

SpecimenCollectionType = create_fhir_type(
    "SpecimenCollectionType", "fhir.resources.specimen.SpecimenCollection"
)

SpecimenContainerType = create_fhir_type(
    "SpecimenContainerType", "fhir.resources.specimen.SpecimenContainer"
)

SpecimenDefinitionType = create_fhir_type(
    "SpecimenDefinitionType", "fhir.resources.specimendefinition.SpecimenDefinition"
)

SpecimenDefinitionTypeTestedType = create_fhir_type(
    "SpecimenDefinitionTypeTestedType",
    "fhir.resources.specimendefinition.SpecimenDefinitionTypeTested",
)

SpecimenDefinitionTypeTestedContainerType = create_fhir_type(
    "SpecimenDefinitionTypeTestedContainerType",
    "fhir.resources.specimendefinition.SpecimenDefinitionTypeTestedContainer",
)

SpecimenDefinitionTypeTestedContainerAdditiveType = create_fhir_type(
    "SpecimenDefinitionTypeTestedContainerAdditiveType",
    "fhir.resources.specimendefinition.SpecimenDefinitionTypeTestedContainerAdditive",
)

SpecimenDefinitionTypeTestedHandlingType = create_fhir_type(
    "SpecimenDefinitionTypeTestedHandlingType",
    "fhir.resources.specimendefinition.SpecimenDefinitionTypeTestedHandling",
)

SpecimenFeatureType = create_fhir_type(
    "SpecimenFeatureType", "fhir.resources.specimen.SpecimenFeature"
)

SpecimenProcessingType = create_fhir_type(
    "SpecimenProcessingType", "fhir.resources.specimen.SpecimenProcessing"
)

StructureDefinitionType = create_fhir_type(
    "StructureDefinitionType", "fhir.resources.structuredefinition.StructureDefinition"
)

StructureDefinitionContextType = create_fhir_type(
    "StructureDefinitionContextType",
    "fhir.resources.structuredefinition.StructureDefinitionContext",
)

StructureDefinitionDifferentialType = create_fhir_type(
    "StructureDefinitionDifferentialType",
    "fhir.resources.structuredefinition.StructureDefinitionDifferential",
)

StructureDefinitionMappingType = create_fhir_type(
    "StructureDefinitionMappingType",
    "fhir.resources.structuredefinition.StructureDefinitionMapping",
)

StructureDefinitionSnapshotType = create_fhir_type(
    "StructureDefinitionSnapshotType",
    "fhir.resources.structuredefinition.StructureDefinitionSnapshot",
)

StructureMapType = create_fhir_type(
    "StructureMapType", "fhir.resources.structuremap.StructureMap"
)

StructureMapConstType = create_fhir_type(
    "StructureMapConstType", "fhir.resources.structuremap.StructureMapConst"
)

StructureMapGroupType = create_fhir_type(
    "StructureMapGroupType", "fhir.resources.structuremap.StructureMapGroup"
)

StructureMapGroupInputType = create_fhir_type(
    "StructureMapGroupInputType", "fhir.resources.structuremap.StructureMapGroupInput"
)

StructureMapGroupRuleType = create_fhir_type(
    "StructureMapGroupRuleType", "fhir.resources.structuremap.StructureMapGroupRule"
)

StructureMapGroupRuleDependentType = create_fhir_type(
    "StructureMapGroupRuleDependentType",
    "fhir.resources.structuremap.StructureMapGroupRuleDependent",
)

StructureMapGroupRuleSourceType = create_fhir_type(
    "StructureMapGroupRuleSourceType",
    "fhir.resources.structuremap.StructureMapGroupRuleSource",
)

StructureMapGroupRuleTargetType = create_fhir_type(
    "StructureMapGroupRuleTargetType",
    "fhir.resources.structuremap.StructureMapGroupRuleTarget",
)

StructureMapGroupRuleTargetParameterType = create_fhir_type(
    "StructureMapGroupRuleTargetParameterType",
    "fhir.resources.structuremap.StructureMapGroupRuleTargetParameter",
)

StructureMapStructureType = create_fhir_type(
    "StructureMapStructureType", "fhir.resources.structuremap.StructureMapStructure"
)

SubscriptionType = create_fhir_type(
    "SubscriptionType", "fhir.resources.subscription.Subscription"
)

SubscriptionFilterByType = create_fhir_type(
    "SubscriptionFilterByType", "fhir.resources.subscription.SubscriptionFilterBy"
)

SubscriptionParameterType = create_fhir_type(
    "SubscriptionParameterType", "fhir.resources.subscription.SubscriptionParameter"
)

SubscriptionStatusType = create_fhir_type(
    "SubscriptionStatusType", "fhir.resources.subscriptionstatus.SubscriptionStatus"
)

SubscriptionStatusNotificationEventType = create_fhir_type(
    "SubscriptionStatusNotificationEventType",
    "fhir.resources.subscriptionstatus.SubscriptionStatusNotificationEvent",
)

SubscriptionTopicType = create_fhir_type(
    "SubscriptionTopicType", "fhir.resources.subscriptiontopic.SubscriptionTopic"
)

SubscriptionTopicCanFilterByType = create_fhir_type(
    "SubscriptionTopicCanFilterByType",
    "fhir.resources.subscriptiontopic.SubscriptionTopicCanFilterBy",
)

SubscriptionTopicEventTriggerType = create_fhir_type(
    "SubscriptionTopicEventTriggerType",
    "fhir.resources.subscriptiontopic.SubscriptionTopicEventTrigger",
)

SubscriptionTopicNotificationShapeType = create_fhir_type(
    "SubscriptionTopicNotificationShapeType",
    "fhir.resources.subscriptiontopic.SubscriptionTopicNotificationShape",
)

SubscriptionTopicResourceTriggerType = create_fhir_type(
    "SubscriptionTopicResourceTriggerType",
    "fhir.resources.subscriptiontopic.SubscriptionTopicResourceTrigger",
)

SubscriptionTopicResourceTriggerQueryCriteriaType = create_fhir_type(
    "SubscriptionTopicResourceTriggerQueryCriteriaType",
    "fhir.resources.subscriptiontopic.SubscriptionTopicResourceTriggerQueryCriteria",
)

SubstanceType = create_fhir_type("SubstanceType", "fhir.resources.substance.Substance")

SubstanceDefinitionType = create_fhir_type(
    "SubstanceDefinitionType", "fhir.resources.substancedefinition.SubstanceDefinition"
)

SubstanceDefinitionCharacterizationType = create_fhir_type(
    "SubstanceDefinitionCharacterizationType",
    "fhir.resources.substancedefinition.SubstanceDefinitionCharacterization",
)

SubstanceDefinitionCodeType = create_fhir_type(
    "SubstanceDefinitionCodeType",
    "fhir.resources.substancedefinition.SubstanceDefinitionCode",
)

SubstanceDefinitionMoietyType = create_fhir_type(
    "SubstanceDefinitionMoietyType",
    "fhir.resources.substancedefinition.SubstanceDefinitionMoiety",
)

SubstanceDefinitionMolecularWeightType = create_fhir_type(
    "SubstanceDefinitionMolecularWeightType",
    "fhir.resources.substancedefinition.SubstanceDefinitionMolecularWeight",
)

SubstanceDefinitionNameType = create_fhir_type(
    "SubstanceDefinitionNameType",
    "fhir.resources.substancedefinition.SubstanceDefinitionName",
)

SubstanceDefinitionNameOfficialType = create_fhir_type(
    "SubstanceDefinitionNameOfficialType",
    "fhir.resources.substancedefinition.SubstanceDefinitionNameOfficial",
)

SubstanceDefinitionPropertyType = create_fhir_type(
    "SubstanceDefinitionPropertyType",
    "fhir.resources.substancedefinition.SubstanceDefinitionProperty",
)

SubstanceDefinitionRelationshipType = create_fhir_type(
    "SubstanceDefinitionRelationshipType",
    "fhir.resources.substancedefinition.SubstanceDefinitionRelationship",
)

SubstanceDefinitionSourceMaterialType = create_fhir_type(
    "SubstanceDefinitionSourceMaterialType",
    "fhir.resources.substancedefinition.SubstanceDefinitionSourceMaterial",
)

SubstanceDefinitionStructureType = create_fhir_type(
    "SubstanceDefinitionStructureType",
    "fhir.resources.substancedefinition.SubstanceDefinitionStructure",
)

SubstanceDefinitionStructureRepresentationType = create_fhir_type(
    "SubstanceDefinitionStructureRepresentationType",
    "fhir.resources.substancedefinition.SubstanceDefinitionStructureRepresentation",
)

SubstanceIngredientType = create_fhir_type(
    "SubstanceIngredientType", "fhir.resources.substance.SubstanceIngredient"
)

SubstanceNucleicAcidType = create_fhir_type(
    "SubstanceNucleicAcidType",
    "fhir.resources.substancenucleicacid.SubstanceNucleicAcid",
)

SubstanceNucleicAcidSubunitType = create_fhir_type(
    "SubstanceNucleicAcidSubunitType",
    "fhir.resources.substancenucleicacid.SubstanceNucleicAcidSubunit",
)

SubstanceNucleicAcidSubunitLinkageType = create_fhir_type(
    "SubstanceNucleicAcidSubunitLinkageType",
    "fhir.resources.substancenucleicacid.SubstanceNucleicAcidSubunitLinkage",
)

SubstanceNucleicAcidSubunitSugarType = create_fhir_type(
    "SubstanceNucleicAcidSubunitSugarType",
    "fhir.resources.substancenucleicacid.SubstanceNucleicAcidSubunitSugar",
)

SubstancePolymerType = create_fhir_type(
    "SubstancePolymerType", "fhir.resources.substancepolymer.SubstancePolymer"
)

SubstancePolymerMonomerSetType = create_fhir_type(
    "SubstancePolymerMonomerSetType",
    "fhir.resources.substancepolymer.SubstancePolymerMonomerSet",
)

SubstancePolymerMonomerSetStartingMaterialType = create_fhir_type(
    "SubstancePolymerMonomerSetStartingMaterialType",
    "fhir.resources.substancepolymer.SubstancePolymerMonomerSetStartingMaterial",
)

SubstancePolymerRepeatType = create_fhir_type(
    "SubstancePolymerRepeatType",
    "fhir.resources.substancepolymer.SubstancePolymerRepeat",
)

SubstancePolymerRepeatRepeatUnitType = create_fhir_type(
    "SubstancePolymerRepeatRepeatUnitType",
    "fhir.resources.substancepolymer.SubstancePolymerRepeatRepeatUnit",
)

SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisationType = create_fhir_type(
    "SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisationType",
    "fhir.resources.substancepolymer.SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation",
)

SubstancePolymerRepeatRepeatUnitStructuralRepresentationType = create_fhir_type(
    "SubstancePolymerRepeatRepeatUnitStructuralRepresentationType",
    "fhir.resources.substancepolymer.SubstancePolymerRepeatRepeatUnitStructuralRepresentation",
)

SubstanceProteinType = create_fhir_type(
    "SubstanceProteinType", "fhir.resources.substanceprotein.SubstanceProtein"
)

SubstanceProteinSubunitType = create_fhir_type(
    "SubstanceProteinSubunitType",
    "fhir.resources.substanceprotein.SubstanceProteinSubunit",
)

SubstanceReferenceInformationType = create_fhir_type(
    "SubstanceReferenceInformationType",
    "fhir.resources.substancereferenceinformation.SubstanceReferenceInformation",
)

SubstanceReferenceInformationGeneType = create_fhir_type(
    "SubstanceReferenceInformationGeneType",
    "fhir.resources.substancereferenceinformation.SubstanceReferenceInformationGene",
)

SubstanceReferenceInformationGeneElementType = create_fhir_type(
    "SubstanceReferenceInformationGeneElementType",
    "fhir.resources.substancereferenceinformation.SubstanceReferenceInformationGeneElement",
)

SubstanceReferenceInformationTargetType = create_fhir_type(
    "SubstanceReferenceInformationTargetType",
    "fhir.resources.substancereferenceinformation.SubstanceReferenceInformationTarget",
)

SubstanceSourceMaterialType = create_fhir_type(
    "SubstanceSourceMaterialType",
    "fhir.resources.substancesourcematerial.SubstanceSourceMaterial",
)

SubstanceSourceMaterialFractionDescriptionType = create_fhir_type(
    "SubstanceSourceMaterialFractionDescriptionType",
    "fhir.resources.substancesourcematerial.SubstanceSourceMaterialFractionDescription",
)

SubstanceSourceMaterialOrganismType = create_fhir_type(
    "SubstanceSourceMaterialOrganismType",
    "fhir.resources.substancesourcematerial.SubstanceSourceMaterialOrganism",
)

SubstanceSourceMaterialOrganismAuthorType = create_fhir_type(
    "SubstanceSourceMaterialOrganismAuthorType",
    "fhir.resources.substancesourcematerial.SubstanceSourceMaterialOrganismAuthor",
)

SubstanceSourceMaterialOrganismHybridType = create_fhir_type(
    "SubstanceSourceMaterialOrganismHybridType",
    "fhir.resources.substancesourcematerial.SubstanceSourceMaterialOrganismHybrid",
)

SubstanceSourceMaterialOrganismOrganismGeneralType = create_fhir_type(
    "SubstanceSourceMaterialOrganismOrganismGeneralType",
    "fhir.resources.substancesourcematerial.SubstanceSourceMaterialOrganismOrganismGeneral",
)

SubstanceSourceMaterialPartDescriptionType = create_fhir_type(
    "SubstanceSourceMaterialPartDescriptionType",
    "fhir.resources.substancesourcematerial.SubstanceSourceMaterialPartDescription",
)

SupplyDeliveryType = create_fhir_type(
    "SupplyDeliveryType", "fhir.resources.supplydelivery.SupplyDelivery"
)

SupplyDeliverySuppliedItemType = create_fhir_type(
    "SupplyDeliverySuppliedItemType",
    "fhir.resources.supplydelivery.SupplyDeliverySuppliedItem",
)

SupplyRequestType = create_fhir_type(
    "SupplyRequestType", "fhir.resources.supplyrequest.SupplyRequest"
)

SupplyRequestParameterType = create_fhir_type(
    "SupplyRequestParameterType", "fhir.resources.supplyrequest.SupplyRequestParameter"
)

TaskType = create_fhir_type("TaskType", "fhir.resources.task.Task")

TaskInputType = create_fhir_type("TaskInputType", "fhir.resources.task.TaskInput")

TaskOutputType = create_fhir_type("TaskOutputType", "fhir.resources.task.TaskOutput")

TaskPerformerType = create_fhir_type(
    "TaskPerformerType", "fhir.resources.task.TaskPerformer"
)

TaskRestrictionType = create_fhir_type(
    "TaskRestrictionType", "fhir.resources.task.TaskRestriction"
)

TerminologyCapabilitiesType = create_fhir_type(
    "TerminologyCapabilitiesType",
    "fhir.resources.terminologycapabilities.TerminologyCapabilities",
)

TerminologyCapabilitiesClosureType = create_fhir_type(
    "TerminologyCapabilitiesClosureType",
    "fhir.resources.terminologycapabilities.TerminologyCapabilitiesClosure",
)

TerminologyCapabilitiesCodeSystemType = create_fhir_type(
    "TerminologyCapabilitiesCodeSystemType",
    "fhir.resources.terminologycapabilities.TerminologyCapabilitiesCodeSystem",
)

TerminologyCapabilitiesCodeSystemVersionType = create_fhir_type(
    "TerminologyCapabilitiesCodeSystemVersionType",
    "fhir.resources.terminologycapabilities.TerminologyCapabilitiesCodeSystemVersion",
)

TerminologyCapabilitiesCodeSystemVersionFilterType = create_fhir_type(
    "TerminologyCapabilitiesCodeSystemVersionFilterType",
    "fhir.resources.terminologycapabilities.TerminologyCapabilitiesCodeSystemVersionFilter",
)

TerminologyCapabilitiesExpansionType = create_fhir_type(
    "TerminologyCapabilitiesExpansionType",
    "fhir.resources.terminologycapabilities.TerminologyCapabilitiesExpansion",
)

TerminologyCapabilitiesExpansionParameterType = create_fhir_type(
    "TerminologyCapabilitiesExpansionParameterType",
    "fhir.resources.terminologycapabilities.TerminologyCapabilitiesExpansionParameter",
)

TerminologyCapabilitiesImplementationType = create_fhir_type(
    "TerminologyCapabilitiesImplementationType",
    "fhir.resources.terminologycapabilities.TerminologyCapabilitiesImplementation",
)

TerminologyCapabilitiesSoftwareType = create_fhir_type(
    "TerminologyCapabilitiesSoftwareType",
    "fhir.resources.terminologycapabilities.TerminologyCapabilitiesSoftware",
)

TerminologyCapabilitiesTranslationType = create_fhir_type(
    "TerminologyCapabilitiesTranslationType",
    "fhir.resources.terminologycapabilities.TerminologyCapabilitiesTranslation",
)

TerminologyCapabilitiesValidateCodeType = create_fhir_type(
    "TerminologyCapabilitiesValidateCodeType",
    "fhir.resources.terminologycapabilities.TerminologyCapabilitiesValidateCode",
)

TestPlanType = create_fhir_type("TestPlanType", "fhir.resources.testplan.TestPlan")

TestPlanDependencyType = create_fhir_type(
    "TestPlanDependencyType", "fhir.resources.testplan.TestPlanDependency"
)

TestPlanTestCaseType = create_fhir_type(
    "TestPlanTestCaseType", "fhir.resources.testplan.TestPlanTestCase"
)

TestPlanTestCaseAssertionType = create_fhir_type(
    "TestPlanTestCaseAssertionType", "fhir.resources.testplan.TestPlanTestCaseAssertion"
)

TestPlanTestCaseDependencyType = create_fhir_type(
    "TestPlanTestCaseDependencyType",
    "fhir.resources.testplan.TestPlanTestCaseDependency",
)

TestPlanTestCaseTestDataType = create_fhir_type(
    "TestPlanTestCaseTestDataType", "fhir.resources.testplan.TestPlanTestCaseTestData"
)

TestPlanTestCaseTestRunType = create_fhir_type(
    "TestPlanTestCaseTestRunType", "fhir.resources.testplan.TestPlanTestCaseTestRun"
)

TestPlanTestCaseTestRunScriptType = create_fhir_type(
    "TestPlanTestCaseTestRunScriptType",
    "fhir.resources.testplan.TestPlanTestCaseTestRunScript",
)

TestReportType = create_fhir_type(
    "TestReportType", "fhir.resources.testreport.TestReport"
)

TestReportParticipantType = create_fhir_type(
    "TestReportParticipantType", "fhir.resources.testreport.TestReportParticipant"
)

TestReportSetupType = create_fhir_type(
    "TestReportSetupType", "fhir.resources.testreport.TestReportSetup"
)

TestReportSetupActionType = create_fhir_type(
    "TestReportSetupActionType", "fhir.resources.testreport.TestReportSetupAction"
)

TestReportSetupActionAssertType = create_fhir_type(
    "TestReportSetupActionAssertType",
    "fhir.resources.testreport.TestReportSetupActionAssert",
)

TestReportSetupActionAssertRequirementType = create_fhir_type(
    "TestReportSetupActionAssertRequirementType",
    "fhir.resources.testreport.TestReportSetupActionAssertRequirement",
)

TestReportSetupActionOperationType = create_fhir_type(
    "TestReportSetupActionOperationType",
    "fhir.resources.testreport.TestReportSetupActionOperation",
)

TestReportTeardownType = create_fhir_type(
    "TestReportTeardownType", "fhir.resources.testreport.TestReportTeardown"
)

TestReportTeardownActionType = create_fhir_type(
    "TestReportTeardownActionType", "fhir.resources.testreport.TestReportTeardownAction"
)

TestReportTestType = create_fhir_type(
    "TestReportTestType", "fhir.resources.testreport.TestReportTest"
)

TestReportTestActionType = create_fhir_type(
    "TestReportTestActionType", "fhir.resources.testreport.TestReportTestAction"
)

TestScriptType = create_fhir_type(
    "TestScriptType", "fhir.resources.testscript.TestScript"
)

TestScriptDestinationType = create_fhir_type(
    "TestScriptDestinationType", "fhir.resources.testscript.TestScriptDestination"
)

TestScriptFixtureType = create_fhir_type(
    "TestScriptFixtureType", "fhir.resources.testscript.TestScriptFixture"
)

TestScriptMetadataType = create_fhir_type(
    "TestScriptMetadataType", "fhir.resources.testscript.TestScriptMetadata"
)

TestScriptMetadataCapabilityType = create_fhir_type(
    "TestScriptMetadataCapabilityType",
    "fhir.resources.testscript.TestScriptMetadataCapability",
)

TestScriptMetadataLinkType = create_fhir_type(
    "TestScriptMetadataLinkType", "fhir.resources.testscript.TestScriptMetadataLink"
)

TestScriptOriginType = create_fhir_type(
    "TestScriptOriginType", "fhir.resources.testscript.TestScriptOrigin"
)

TestScriptScopeType = create_fhir_type(
    "TestScriptScopeType", "fhir.resources.testscript.TestScriptScope"
)

TestScriptSetupType = create_fhir_type(
    "TestScriptSetupType", "fhir.resources.testscript.TestScriptSetup"
)

TestScriptSetupActionType = create_fhir_type(
    "TestScriptSetupActionType", "fhir.resources.testscript.TestScriptSetupAction"
)

TestScriptSetupActionAssertType = create_fhir_type(
    "TestScriptSetupActionAssertType",
    "fhir.resources.testscript.TestScriptSetupActionAssert",
)

TestScriptSetupActionAssertRequirementType = create_fhir_type(
    "TestScriptSetupActionAssertRequirementType",
    "fhir.resources.testscript.TestScriptSetupActionAssertRequirement",
)

TestScriptSetupActionOperationType = create_fhir_type(
    "TestScriptSetupActionOperationType",
    "fhir.resources.testscript.TestScriptSetupActionOperation",
)

TestScriptSetupActionOperationRequestHeaderType = create_fhir_type(
    "TestScriptSetupActionOperationRequestHeaderType",
    "fhir.resources.testscript.TestScriptSetupActionOperationRequestHeader",
)

TestScriptTeardownType = create_fhir_type(
    "TestScriptTeardownType", "fhir.resources.testscript.TestScriptTeardown"
)

TestScriptTeardownActionType = create_fhir_type(
    "TestScriptTeardownActionType", "fhir.resources.testscript.TestScriptTeardownAction"
)

TestScriptTestType = create_fhir_type(
    "TestScriptTestType", "fhir.resources.testscript.TestScriptTest"
)

TestScriptTestActionType = create_fhir_type(
    "TestScriptTestActionType", "fhir.resources.testscript.TestScriptTestAction"
)

TestScriptVariableType = create_fhir_type(
    "TestScriptVariableType", "fhir.resources.testscript.TestScriptVariable"
)

TimingType = create_fhir_type("TimingType", "fhir.resources.timing.Timing")

TimingRepeatType = create_fhir_type(
    "TimingRepeatType", "fhir.resources.timing.TimingRepeat"
)

TransportType = create_fhir_type("TransportType", "fhir.resources.transport.Transport")

TransportInputType = create_fhir_type(
    "TransportInputType", "fhir.resources.transport.TransportInput"
)

TransportOutputType = create_fhir_type(
    "TransportOutputType", "fhir.resources.transport.TransportOutput"
)

TransportRestrictionType = create_fhir_type(
    "TransportRestrictionType", "fhir.resources.transport.TransportRestriction"
)

TriggerDefinitionType = create_fhir_type(
    "TriggerDefinitionType", "fhir.resources.triggerdefinition.TriggerDefinition"
)

UsageContextType = create_fhir_type(
    "UsageContextType", "fhir.resources.usagecontext.UsageContext"
)

ValueSetType = create_fhir_type("ValueSetType", "fhir.resources.valueset.ValueSet")

ValueSetComposeType = create_fhir_type(
    "ValueSetComposeType", "fhir.resources.valueset.ValueSetCompose"
)

ValueSetComposeIncludeType = create_fhir_type(
    "ValueSetComposeIncludeType", "fhir.resources.valueset.ValueSetComposeInclude"
)

ValueSetComposeIncludeConceptType = create_fhir_type(
    "ValueSetComposeIncludeConceptType",
    "fhir.resources.valueset.ValueSetComposeIncludeConcept",
)

ValueSetComposeIncludeConceptDesignationType = create_fhir_type(
    "ValueSetComposeIncludeConceptDesignationType",
    "fhir.resources.valueset.ValueSetComposeIncludeConceptDesignation",
)

ValueSetComposeIncludeFilterType = create_fhir_type(
    "ValueSetComposeIncludeFilterType",
    "fhir.resources.valueset.ValueSetComposeIncludeFilter",
)

ValueSetExpansionType = create_fhir_type(
    "ValueSetExpansionType", "fhir.resources.valueset.ValueSetExpansion"
)

ValueSetExpansionContainsType = create_fhir_type(
    "ValueSetExpansionContainsType", "fhir.resources.valueset.ValueSetExpansionContains"
)

ValueSetExpansionContainsPropertyType = create_fhir_type(
    "ValueSetExpansionContainsPropertyType",
    "fhir.resources.valueset.ValueSetExpansionContainsProperty",
)

ValueSetExpansionContainsPropertySubPropertyType = create_fhir_type(
    "ValueSetExpansionContainsPropertySubPropertyType",
    "fhir.resources.valueset.ValueSetExpansionContainsPropertySubProperty",
)

ValueSetExpansionParameterType = create_fhir_type(
    "ValueSetExpansionParameterType",
    "fhir.resources.valueset.ValueSetExpansionParameter",
)

ValueSetExpansionPropertyType = create_fhir_type(
    "ValueSetExpansionPropertyType", "fhir.resources.valueset.ValueSetExpansionProperty"
)

ValueSetScopeType = create_fhir_type(
    "ValueSetScopeType", "fhir.resources.valueset.ValueSetScope"
)

VerificationResultType = create_fhir_type(
    "VerificationResultType", "fhir.resources.verificationresult.VerificationResult"
)

VerificationResultAttestationType = create_fhir_type(
    "VerificationResultAttestationType",
    "fhir.resources.verificationresult.VerificationResultAttestation",
)

VerificationResultPrimarySourceType = create_fhir_type(
    "VerificationResultPrimarySourceType",
    "fhir.resources.verificationresult.VerificationResultPrimarySource",
)

VerificationResultValidatorType = create_fhir_type(
    "VerificationResultValidatorType",
    "fhir.resources.verificationresult.VerificationResultValidator",
)

VirtualServiceDetailType = create_fhir_type(
    "VirtualServiceDetailType",
    "fhir.resources.virtualservicedetail.VirtualServiceDetail",
)

VisionPrescriptionType = create_fhir_type(
    "VisionPrescriptionType", "fhir.resources.visionprescription.VisionPrescription"
)

VisionPrescriptionLensSpecificationType = create_fhir_type(
    "VisionPrescriptionLensSpecificationType",
    "fhir.resources.visionprescription.VisionPrescriptionLensSpecification",
)

VisionPrescriptionLensSpecificationPrismType = create_fhir_type(
    "VisionPrescriptionLensSpecificationPrismType",
    "fhir.resources.visionprescription.VisionPrescriptionLensSpecificationPrism",
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
    "AccountBalanceType",
    "AccountCoverageType",
    "AccountDiagnosisType",
    "AccountGuarantorType",
    "AccountProcedureType",
    "AccountRelatedAccountType",
    "ActivityDefinitionType",
    "ActivityDefinitionDynamicValueType",
    "ActivityDefinitionParticipantType",
    "ActorDefinitionType",
    "AddressType",
    "AdministrableProductDefinitionType",
    "AdministrableProductDefinitionPropertyType",
    "AdministrableProductDefinitionRouteOfAdministrationType",
    "AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesType",
    "AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriodType",
    "AdverseEventType",
    "AdverseEventContributingFactorType",
    "AdverseEventMitigatingActionType",
    "AdverseEventParticipantType",
    "AdverseEventPreventiveActionType",
    "AdverseEventSupportingInfoType",
    "AdverseEventSuspectEntityType",
    "AdverseEventSuspectEntityCausalityType",
    "AgeType",
    "AllergyIntoleranceType",
    "AllergyIntoleranceParticipantType",
    "AllergyIntoleranceReactionType",
    "AnnotationType",
    "AppointmentType",
    "AppointmentParticipantType",
    "AppointmentRecurrenceTemplateType",
    "AppointmentRecurrenceTemplateMonthlyTemplateType",
    "AppointmentRecurrenceTemplateWeeklyTemplateType",
    "AppointmentRecurrenceTemplateYearlyTemplateType",
    "AppointmentResponseType",
    "ArtifactAssessmentType",
    "ArtifactAssessmentContentType",
    "AttachmentType",
    "AuditEventType",
    "AuditEventAgentType",
    "AuditEventEntityType",
    "AuditEventEntityDetailType",
    "AuditEventOutcomeType",
    "AuditEventSourceType",
    "AvailabilityType",
    "AvailabilityAvailableTimeType",
    "AvailabilityNotAvailableTimeType",
    "BackboneElementType",
    "BackboneTypeType",
    "BaseType",
    "BasicType",
    "BinaryType",
    "BiologicallyDerivedProductType",
    "BiologicallyDerivedProductCollectionType",
    "BiologicallyDerivedProductDispenseType",
    "BiologicallyDerivedProductDispensePerformerType",
    "BiologicallyDerivedProductPropertyType",
    "BodyStructureType",
    "BodyStructureIncludedStructureType",
    "BodyStructureIncludedStructureBodyLandmarkOrientationType",
    "BodyStructureIncludedStructureBodyLandmarkOrientationDistanceFromLandmarkType",
    "BundleType",
    "BundleEntryType",
    "BundleEntryRequestType",
    "BundleEntryResponseType",
    "BundleEntrySearchType",
    "BundleLinkType",
    "CanonicalResourceType",
    "CapabilityStatementType",
    "CapabilityStatementDocumentType",
    "CapabilityStatementImplementationType",
    "CapabilityStatementMessagingType",
    "CapabilityStatementMessagingEndpointType",
    "CapabilityStatementMessagingSupportedMessageType",
    "CapabilityStatementRestType",
    "CapabilityStatementRestInteractionType",
    "CapabilityStatementRestResourceType",
    "CapabilityStatementRestResourceInteractionType",
    "CapabilityStatementRestResourceOperationType",
    "CapabilityStatementRestResourceSearchParamType",
    "CapabilityStatementRestSecurityType",
    "CapabilityStatementSoftwareType",
    "CarePlanType",
    "CarePlanActivityType",
    "CareTeamType",
    "CareTeamParticipantType",
    "ChargeItemType",
    "ChargeItemDefinitionType",
    "ChargeItemDefinitionApplicabilityType",
    "ChargeItemDefinitionPropertyGroupType",
    "ChargeItemPerformerType",
    "CitationType",
    "CitationCitedArtifactType",
    "CitationCitedArtifactAbstractType",
    "CitationCitedArtifactClassificationType",
    "CitationCitedArtifactContributorshipType",
    "CitationCitedArtifactContributorshipEntryType",
    "CitationCitedArtifactContributorshipEntryContributionInstanceType",
    "CitationCitedArtifactContributorshipSummaryType",
    "CitationCitedArtifactPartType",
    "CitationCitedArtifactPublicationFormType",
    "CitationCitedArtifactPublicationFormPublishedInType",
    "CitationCitedArtifactRelatesToType",
    "CitationCitedArtifactStatusDateType",
    "CitationCitedArtifactTitleType",
    "CitationCitedArtifactVersionType",
    "CitationCitedArtifactWebLocationType",
    "CitationClassificationType",
    "CitationStatusDateType",
    "CitationSummaryType",
    "ClaimType",
    "ClaimAccidentType",
    "ClaimCareTeamType",
    "ClaimDiagnosisType",
    "ClaimEventType",
    "ClaimInsuranceType",
    "ClaimItemType",
    "ClaimItemBodySiteType",
    "ClaimItemDetailType",
    "ClaimItemDetailSubDetailType",
    "ClaimPayeeType",
    "ClaimProcedureType",
    "ClaimRelatedType",
    "ClaimResponseType",
    "ClaimResponseAddItemType",
    "ClaimResponseAddItemBodySiteType",
    "ClaimResponseAddItemDetailType",
    "ClaimResponseAddItemDetailSubDetailType",
    "ClaimResponseErrorType",
    "ClaimResponseEventType",
    "ClaimResponseInsuranceType",
    "ClaimResponseItemType",
    "ClaimResponseItemAdjudicationType",
    "ClaimResponseItemDetailType",
    "ClaimResponseItemDetailSubDetailType",
    "ClaimResponseItemReviewOutcomeType",
    "ClaimResponsePaymentType",
    "ClaimResponseProcessNoteType",
    "ClaimResponseTotalType",
    "ClaimSupportingInfoType",
    "ClinicalImpressionType",
    "ClinicalImpressionFindingType",
    "ClinicalUseDefinitionType",
    "ClinicalUseDefinitionContraindicationType",
    "ClinicalUseDefinitionContraindicationOtherTherapyType",
    "ClinicalUseDefinitionIndicationType",
    "ClinicalUseDefinitionInteractionType",
    "ClinicalUseDefinitionInteractionInteractantType",
    "ClinicalUseDefinitionUndesirableEffectType",
    "ClinicalUseDefinitionWarningType",
    "CodeSystemType",
    "CodeSystemConceptType",
    "CodeSystemConceptDesignationType",
    "CodeSystemConceptPropertyType",
    "CodeSystemFilterType",
    "CodeSystemPropertyType",
    "CodeableConceptType",
    "CodeableReferenceType",
    "CodingType",
    "CommunicationType",
    "CommunicationPayloadType",
    "CommunicationRequestType",
    "CommunicationRequestPayloadType",
    "CompartmentDefinitionType",
    "CompartmentDefinitionResourceType",
    "CompositionType",
    "CompositionAttesterType",
    "CompositionEventType",
    "CompositionSectionType",
    "ConceptMapType",
    "ConceptMapAdditionalAttributeType",
    "ConceptMapGroupType",
    "ConceptMapGroupElementType",
    "ConceptMapGroupElementTargetType",
    "ConceptMapGroupElementTargetDependsOnType",
    "ConceptMapGroupElementTargetPropertyType",
    "ConceptMapGroupUnmappedType",
    "ConceptMapPropertyType",
    "ConditionType",
    "ConditionDefinitionType",
    "ConditionDefinitionMedicationType",
    "ConditionDefinitionObservationType",
    "ConditionDefinitionPlanType",
    "ConditionDefinitionPreconditionType",
    "ConditionDefinitionQuestionnaireType",
    "ConditionParticipantType",
    "ConditionStageType",
    "ConsentType",
    "ConsentPolicyBasisType",
    "ConsentProvisionType",
    "ConsentProvisionActorType",
    "ConsentProvisionDataType",
    "ConsentVerificationType",
    "ContactDetailType",
    "ContactPointType",
    "ContractType",
    "ContractContentDefinitionType",
    "ContractFriendlyType",
    "ContractLegalType",
    "ContractRuleType",
    "ContractSignerType",
    "ContractTermType",
    "ContractTermActionType",
    "ContractTermActionSubjectType",
    "ContractTermAssetType",
    "ContractTermAssetContextType",
    "ContractTermAssetValuedItemType",
    "ContractTermOfferType",
    "ContractTermOfferAnswerType",
    "ContractTermOfferPartyType",
    "ContractTermSecurityLabelType",
    "ContributorType",
    "CountType",
    "CoverageType",
    "CoverageClassType",
    "CoverageCostToBeneficiaryType",
    "CoverageCostToBeneficiaryExceptionType",
    "CoverageEligibilityRequestType",
    "CoverageEligibilityRequestEventType",
    "CoverageEligibilityRequestInsuranceType",
    "CoverageEligibilityRequestItemType",
    "CoverageEligibilityRequestItemDiagnosisType",
    "CoverageEligibilityRequestSupportingInfoType",
    "CoverageEligibilityResponseType",
    "CoverageEligibilityResponseErrorType",
    "CoverageEligibilityResponseEventType",
    "CoverageEligibilityResponseInsuranceType",
    "CoverageEligibilityResponseInsuranceItemType",
    "CoverageEligibilityResponseInsuranceItemBenefitType",
    "CoveragePaymentByType",
    "DataRequirementType",
    "DataRequirementCodeFilterType",
    "DataRequirementDateFilterType",
    "DataRequirementSortType",
    "DataRequirementValueFilterType",
    "DataTypeType",
    "DetectedIssueType",
    "DetectedIssueEvidenceType",
    "DetectedIssueMitigationType",
    "DeviceType",
    "DeviceAssociationType",
    "DeviceAssociationOperationType",
    "DeviceConformsToType",
    "DeviceDefinitionType",
    "DeviceDefinitionChargeItemType",
    "DeviceDefinitionClassificationType",
    "DeviceDefinitionConformsToType",
    "DeviceDefinitionCorrectiveActionType",
    "DeviceDefinitionDeviceNameType",
    "DeviceDefinitionGuidelineType",
    "DeviceDefinitionHasPartType",
    "DeviceDefinitionLinkType",
    "DeviceDefinitionMaterialType",
    "DeviceDefinitionPackagingType",
    "DeviceDefinitionPackagingDistributorType",
    "DeviceDefinitionPropertyType",
    "DeviceDefinitionRegulatoryIdentifierType",
    "DeviceDefinitionUdiDeviceIdentifierType",
    "DeviceDefinitionUdiDeviceIdentifierMarketDistributionType",
    "DeviceDefinitionVersionType",
    "DeviceDispenseType",
    "DeviceDispensePerformerType",
    "DeviceMetricType",
    "DeviceMetricCalibrationType",
    "DeviceNameType",
    "DevicePropertyType",
    "DeviceRequestType",
    "DeviceRequestParameterType",
    "DeviceUdiCarrierType",
    "DeviceUsageType",
    "DeviceUsageAdherenceType",
    "DeviceVersionType",
    "DiagnosticReportType",
    "DiagnosticReportMediaType",
    "DiagnosticReportSupportingInfoType",
    "DistanceType",
    "DocumentReferenceType",
    "DocumentReferenceAttesterType",
    "DocumentReferenceContentType",
    "DocumentReferenceContentProfileType",
    "DocumentReferenceRelatesToType",
    "DomainResourceType",
    "DosageType",
    "DosageDoseAndRateType",
    "DurationType",
    "ElementType",
    "ElementDefinitionType",
    "ElementDefinitionBaseType",
    "ElementDefinitionBindingType",
    "ElementDefinitionBindingAdditionalType",
    "ElementDefinitionConstraintType",
    "ElementDefinitionExampleType",
    "ElementDefinitionMappingType",
    "ElementDefinitionSlicingType",
    "ElementDefinitionSlicingDiscriminatorType",
    "ElementDefinitionTypeType",
    "EncounterType",
    "EncounterAdmissionType",
    "EncounterDiagnosisType",
    "EncounterHistoryType",
    "EncounterHistoryLocationType",
    "EncounterLocationType",
    "EncounterParticipantType",
    "EncounterReasonType",
    "EndpointType",
    "EndpointPayloadType",
    "EnrollmentRequestType",
    "EnrollmentResponseType",
    "EpisodeOfCareType",
    "EpisodeOfCareDiagnosisType",
    "EpisodeOfCareReasonType",
    "EpisodeOfCareStatusHistoryType",
    "EventDefinitionType",
    "EvidenceType",
    "EvidenceCertaintyType",
    "EvidenceReportType",
    "EvidenceReportRelatesToType",
    "EvidenceReportRelatesToTargetType",
    "EvidenceReportSectionType",
    "EvidenceReportSubjectType",
    "EvidenceReportSubjectCharacteristicType",
    "EvidenceStatisticType",
    "EvidenceStatisticAttributeEstimateType",
    "EvidenceStatisticModelCharacteristicType",
    "EvidenceStatisticModelCharacteristicVariableType",
    "EvidenceStatisticSampleSizeType",
    "EvidenceVariableType",
    "EvidenceVariableCategoryType",
    "EvidenceVariableCharacteristicType",
    "EvidenceVariableCharacteristicDefinitionByCombinationType",
    "EvidenceVariableCharacteristicDefinitionByTypeAndValueType",
    "EvidenceVariableCharacteristicTimeFromEventType",
    "EvidenceVariableDefinitionType",
    "ExampleScenarioType",
    "ExampleScenarioActorType",
    "ExampleScenarioInstanceType",
    "ExampleScenarioInstanceContainedInstanceType",
    "ExampleScenarioInstanceVersionType",
    "ExampleScenarioProcessType",
    "ExampleScenarioProcessStepType",
    "ExampleScenarioProcessStepAlternativeType",
    "ExampleScenarioProcessStepOperationType",
    "ExplanationOfBenefitType",
    "ExplanationOfBenefitAccidentType",
    "ExplanationOfBenefitAddItemType",
    "ExplanationOfBenefitAddItemBodySiteType",
    "ExplanationOfBenefitAddItemDetailType",
    "ExplanationOfBenefitAddItemDetailSubDetailType",
    "ExplanationOfBenefitBenefitBalanceType",
    "ExplanationOfBenefitBenefitBalanceFinancialType",
    "ExplanationOfBenefitCareTeamType",
    "ExplanationOfBenefitDiagnosisType",
    "ExplanationOfBenefitEventType",
    "ExplanationOfBenefitInsuranceType",
    "ExplanationOfBenefitItemType",
    "ExplanationOfBenefitItemAdjudicationType",
    "ExplanationOfBenefitItemBodySiteType",
    "ExplanationOfBenefitItemDetailType",
    "ExplanationOfBenefitItemDetailSubDetailType",
    "ExplanationOfBenefitItemReviewOutcomeType",
    "ExplanationOfBenefitPayeeType",
    "ExplanationOfBenefitPaymentType",
    "ExplanationOfBenefitProcedureType",
    "ExplanationOfBenefitProcessNoteType",
    "ExplanationOfBenefitRelatedType",
    "ExplanationOfBenefitSupportingInfoType",
    "ExplanationOfBenefitTotalType",
    "ExpressionType",
    "ExtendedContactDetailType",
    "ExtensionType",
    "FamilyMemberHistoryType",
    "FamilyMemberHistoryConditionType",
    "FamilyMemberHistoryParticipantType",
    "FamilyMemberHistoryProcedureType",
    "FlagType",
    "FormularyItemType",
    "GenomicStudyType",
    "GenomicStudyAnalysisType",
    "GenomicStudyAnalysisDeviceType",
    "GenomicStudyAnalysisInputType",
    "GenomicStudyAnalysisOutputType",
    "GenomicStudyAnalysisPerformerType",
    "GoalType",
    "GoalTargetType",
    "GraphDefinitionType",
    "GraphDefinitionLinkType",
    "GraphDefinitionLinkCompartmentType",
    "GraphDefinitionNodeType",
    "GroupType",
    "GroupCharacteristicType",
    "GroupMemberType",
    "GuidanceResponseType",
    "HealthcareServiceType",
    "HealthcareServiceEligibilityType",
    "HumanNameType",
    "IdentifierType",
    "ImagingSelectionType",
    "ImagingSelectionInstanceType",
    "ImagingSelectionInstanceImageRegion2DType",
    "ImagingSelectionInstanceImageRegion3DType",
    "ImagingSelectionPerformerType",
    "ImagingStudyType",
    "ImagingStudySeriesType",
    "ImagingStudySeriesInstanceType",
    "ImagingStudySeriesPerformerType",
    "ImmunizationType",
    "ImmunizationEvaluationType",
    "ImmunizationPerformerType",
    "ImmunizationProgramEligibilityType",
    "ImmunizationProtocolAppliedType",
    "ImmunizationReactionType",
    "ImmunizationRecommendationType",
    "ImmunizationRecommendationRecommendationType",
    "ImmunizationRecommendationRecommendationDateCriterionType",
    "ImplementationGuideType",
    "ImplementationGuideDefinitionType",
    "ImplementationGuideDefinitionGroupingType",
    "ImplementationGuideDefinitionPageType",
    "ImplementationGuideDefinitionParameterType",
    "ImplementationGuideDefinitionResourceType",
    "ImplementationGuideDefinitionTemplateType",
    "ImplementationGuideDependsOnType",
    "ImplementationGuideGlobalType",
    "ImplementationGuideManifestType",
    "ImplementationGuideManifestPageType",
    "ImplementationGuideManifestResourceType",
    "IngredientType",
    "IngredientManufacturerType",
    "IngredientSubstanceType",
    "IngredientSubstanceStrengthType",
    "IngredientSubstanceStrengthReferenceStrengthType",
    "InsurancePlanType",
    "InsurancePlanCoverageType",
    "InsurancePlanCoverageBenefitType",
    "InsurancePlanCoverageBenefitLimitType",
    "InsurancePlanPlanType",
    "InsurancePlanPlanGeneralCostType",
    "InsurancePlanPlanSpecificCostType",
    "InsurancePlanPlanSpecificCostBenefitType",
    "InsurancePlanPlanSpecificCostBenefitCostType",
    "InventoryItemType",
    "InventoryItemAssociationType",
    "InventoryItemCharacteristicType",
    "InventoryItemDescriptionType",
    "InventoryItemInstanceType",
    "InventoryItemNameType",
    "InventoryItemResponsibleOrganizationType",
    "InventoryReportType",
    "InventoryReportInventoryListingType",
    "InventoryReportInventoryListingItemType",
    "InvoiceType",
    "InvoiceLineItemType",
    "InvoiceParticipantType",
    "LibraryType",
    "LinkageType",
    "LinkageItemType",
    "ListType",
    "ListEntryType",
    "LocationType",
    "LocationPositionType",
    "ManufacturedItemDefinitionType",
    "ManufacturedItemDefinitionComponentType",
    "ManufacturedItemDefinitionComponentConstituentType",
    "ManufacturedItemDefinitionPropertyType",
    "MarketingStatusType",
    "MeasureType",
    "MeasureGroupType",
    "MeasureGroupPopulationType",
    "MeasureGroupStratifierType",
    "MeasureGroupStratifierComponentType",
    "MeasureReportType",
    "MeasureReportGroupType",
    "MeasureReportGroupPopulationType",
    "MeasureReportGroupStratifierType",
    "MeasureReportGroupStratifierStratumType",
    "MeasureReportGroupStratifierStratumComponentType",
    "MeasureReportGroupStratifierStratumPopulationType",
    "MeasureSupplementalDataType",
    "MeasureTermType",
    "MedicationType",
    "MedicationAdministrationType",
    "MedicationAdministrationDosageType",
    "MedicationAdministrationPerformerType",
    "MedicationBatchType",
    "MedicationDispenseType",
    "MedicationDispensePerformerType",
    "MedicationDispenseSubstitutionType",
    "MedicationIngredientType",
    "MedicationKnowledgeType",
    "MedicationKnowledgeCostType",
    "MedicationKnowledgeDefinitionalType",
    "MedicationKnowledgeDefinitionalDrugCharacteristicType",
    "MedicationKnowledgeDefinitionalIngredientType",
    "MedicationKnowledgeIndicationGuidelineType",
    "MedicationKnowledgeIndicationGuidelineDosingGuidelineType",
    "MedicationKnowledgeIndicationGuidelineDosingGuidelineDosageType",
    "MedicationKnowledgeIndicationGuidelineDosingGuidelinePatientCharacteristicType",
    "MedicationKnowledgeMedicineClassificationType",
    "MedicationKnowledgeMonitoringProgramType",
    "MedicationKnowledgeMonographType",
    "MedicationKnowledgePackagingType",
    "MedicationKnowledgeRegulatoryType",
    "MedicationKnowledgeRegulatoryMaxDispenseType",
    "MedicationKnowledgeRegulatorySubstitutionType",
    "MedicationKnowledgeRelatedMedicationKnowledgeType",
    "MedicationKnowledgeStorageGuidelineType",
    "MedicationKnowledgeStorageGuidelineEnvironmentalSettingType",
    "MedicationRequestType",
    "MedicationRequestDispenseRequestType",
    "MedicationRequestDispenseRequestInitialFillType",
    "MedicationRequestSubstitutionType",
    "MedicationStatementType",
    "MedicationStatementAdherenceType",
    "MedicinalProductDefinitionType",
    "MedicinalProductDefinitionCharacteristicType",
    "MedicinalProductDefinitionContactType",
    "MedicinalProductDefinitionCrossReferenceType",
    "MedicinalProductDefinitionNameType",
    "MedicinalProductDefinitionNamePartType",
    "MedicinalProductDefinitionNameUsageType",
    "MedicinalProductDefinitionOperationType",
    "MessageDefinitionType",
    "MessageDefinitionAllowedResponseType",
    "MessageDefinitionFocusType",
    "MessageHeaderType",
    "MessageHeaderDestinationType",
    "MessageHeaderResponseType",
    "MessageHeaderSourceType",
    "MetaType",
    "MetadataResourceType",
    "MolecularSequenceType",
    "MolecularSequenceRelativeType",
    "MolecularSequenceRelativeEditType",
    "MolecularSequenceRelativeStartingSequenceType",
    "MonetaryComponentType",
    "MoneyType",
    "NamingSystemType",
    "NamingSystemUniqueIdType",
    "NarrativeType",
    "NutritionIntakeType",
    "NutritionIntakeConsumedItemType",
    "NutritionIntakeIngredientLabelType",
    "NutritionIntakePerformerType",
    "NutritionOrderType",
    "NutritionOrderEnteralFormulaType",
    "NutritionOrderEnteralFormulaAdditiveType",
    "NutritionOrderEnteralFormulaAdministrationType",
    "NutritionOrderEnteralFormulaAdministrationScheduleType",
    "NutritionOrderOralDietType",
    "NutritionOrderOralDietNutrientType",
    "NutritionOrderOralDietScheduleType",
    "NutritionOrderOralDietTextureType",
    "NutritionOrderSupplementType",
    "NutritionOrderSupplementScheduleType",
    "NutritionProductType",
    "NutritionProductCharacteristicType",
    "NutritionProductIngredientType",
    "NutritionProductInstanceType",
    "NutritionProductNutrientType",
    "ObservationType",
    "ObservationComponentType",
    "ObservationDefinitionType",
    "ObservationDefinitionComponentType",
    "ObservationDefinitionQualifiedValueType",
    "ObservationReferenceRangeType",
    "ObservationTriggeredByType",
    "OperationDefinitionType",
    "OperationDefinitionOverloadType",
    "OperationDefinitionParameterType",
    "OperationDefinitionParameterBindingType",
    "OperationDefinitionParameterReferencedFromType",
    "OperationOutcomeType",
    "OperationOutcomeIssueType",
    "OrganizationType",
    "OrganizationAffiliationType",
    "OrganizationQualificationType",
    "PackagedProductDefinitionType",
    "PackagedProductDefinitionLegalStatusOfSupplyType",
    "PackagedProductDefinitionPackagingType",
    "PackagedProductDefinitionPackagingContainedItemType",
    "PackagedProductDefinitionPackagingPropertyType",
    "ParameterDefinitionType",
    "ParametersType",
    "ParametersParameterType",
    "PatientType",
    "PatientCommunicationType",
    "PatientContactType",
    "PatientLinkType",
    "PaymentNoticeType",
    "PaymentReconciliationType",
    "PaymentReconciliationAllocationType",
    "PaymentReconciliationProcessNoteType",
    "PeriodType",
    "PermissionType",
    "PermissionJustificationType",
    "PermissionRuleType",
    "PermissionRuleActivityType",
    "PermissionRuleDataType",
    "PermissionRuleDataResourceType",
    "PersonType",
    "PersonCommunicationType",
    "PersonLinkType",
    "PlanDefinitionType",
    "PlanDefinitionActionType",
    "PlanDefinitionActionConditionType",
    "PlanDefinitionActionDynamicValueType",
    "PlanDefinitionActionInputType",
    "PlanDefinitionActionOutputType",
    "PlanDefinitionActionParticipantType",
    "PlanDefinitionActionRelatedActionType",
    "PlanDefinitionActorType",
    "PlanDefinitionActorOptionType",
    "PlanDefinitionGoalType",
    "PlanDefinitionGoalTargetType",
    "PractitionerType",
    "PractitionerCommunicationType",
    "PractitionerQualificationType",
    "PractitionerRoleType",
    "PrimitiveTypeType",
    "ProcedureType",
    "ProcedureFocalDeviceType",
    "ProcedurePerformerType",
    "ProductShelfLifeType",
    "ProvenanceType",
    "ProvenanceAgentType",
    "ProvenanceEntityType",
    "QuantityType",
    "QuestionnaireType",
    "QuestionnaireItemType",
    "QuestionnaireItemAnswerOptionType",
    "QuestionnaireItemEnableWhenType",
    "QuestionnaireItemInitialType",
    "QuestionnaireResponseType",
    "QuestionnaireResponseItemType",
    "QuestionnaireResponseItemAnswerType",
    "RangeType",
    "RatioType",
    "RatioRangeType",
    "ReferenceType",
    "RegulatedAuthorizationType",
    "RegulatedAuthorizationCaseType",
    "RelatedArtifactType",
    "RelatedPersonType",
    "RelatedPersonCommunicationType",
    "RequestOrchestrationType",
    "RequestOrchestrationActionType",
    "RequestOrchestrationActionConditionType",
    "RequestOrchestrationActionDynamicValueType",
    "RequestOrchestrationActionInputType",
    "RequestOrchestrationActionOutputType",
    "RequestOrchestrationActionParticipantType",
    "RequestOrchestrationActionRelatedActionType",
    "RequirementsType",
    "RequirementsStatementType",
    "ResearchStudyType",
    "ResearchStudyAssociatedPartyType",
    "ResearchStudyComparisonGroupType",
    "ResearchStudyLabelType",
    "ResearchStudyObjectiveType",
    "ResearchStudyOutcomeMeasureType",
    "ResearchStudyProgressStatusType",
    "ResearchStudyRecruitmentType",
    "ResearchSubjectType",
    "ResearchSubjectProgressType",
    "ResourceType",
    "RiskAssessmentType",
    "RiskAssessmentPredictionType",
    "SampledDataType",
    "ScheduleType",
    "SearchParameterType",
    "SearchParameterComponentType",
    "ServiceRequestType",
    "ServiceRequestOrderDetailType",
    "ServiceRequestOrderDetailParameterType",
    "ServiceRequestPatientInstructionType",
    "SignatureType",
    "SlotType",
    "SpecimenType",
    "SpecimenCollectionType",
    "SpecimenContainerType",
    "SpecimenDefinitionType",
    "SpecimenDefinitionTypeTestedType",
    "SpecimenDefinitionTypeTestedContainerType",
    "SpecimenDefinitionTypeTestedContainerAdditiveType",
    "SpecimenDefinitionTypeTestedHandlingType",
    "SpecimenFeatureType",
    "SpecimenProcessingType",
    "StructureDefinitionType",
    "StructureDefinitionContextType",
    "StructureDefinitionDifferentialType",
    "StructureDefinitionMappingType",
    "StructureDefinitionSnapshotType",
    "StructureMapType",
    "StructureMapConstType",
    "StructureMapGroupType",
    "StructureMapGroupInputType",
    "StructureMapGroupRuleType",
    "StructureMapGroupRuleDependentType",
    "StructureMapGroupRuleSourceType",
    "StructureMapGroupRuleTargetType",
    "StructureMapGroupRuleTargetParameterType",
    "StructureMapStructureType",
    "SubscriptionType",
    "SubscriptionFilterByType",
    "SubscriptionParameterType",
    "SubscriptionStatusType",
    "SubscriptionStatusNotificationEventType",
    "SubscriptionTopicType",
    "SubscriptionTopicCanFilterByType",
    "SubscriptionTopicEventTriggerType",
    "SubscriptionTopicNotificationShapeType",
    "SubscriptionTopicResourceTriggerType",
    "SubscriptionTopicResourceTriggerQueryCriteriaType",
    "SubstanceType",
    "SubstanceDefinitionType",
    "SubstanceDefinitionCharacterizationType",
    "SubstanceDefinitionCodeType",
    "SubstanceDefinitionMoietyType",
    "SubstanceDefinitionMolecularWeightType",
    "SubstanceDefinitionNameType",
    "SubstanceDefinitionNameOfficialType",
    "SubstanceDefinitionPropertyType",
    "SubstanceDefinitionRelationshipType",
    "SubstanceDefinitionSourceMaterialType",
    "SubstanceDefinitionStructureType",
    "SubstanceDefinitionStructureRepresentationType",
    "SubstanceIngredientType",
    "SubstanceNucleicAcidType",
    "SubstanceNucleicAcidSubunitType",
    "SubstanceNucleicAcidSubunitLinkageType",
    "SubstanceNucleicAcidSubunitSugarType",
    "SubstancePolymerType",
    "SubstancePolymerMonomerSetType",
    "SubstancePolymerMonomerSetStartingMaterialType",
    "SubstancePolymerRepeatType",
    "SubstancePolymerRepeatRepeatUnitType",
    "SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisationType",
    "SubstancePolymerRepeatRepeatUnitStructuralRepresentationType",
    "SubstanceProteinType",
    "SubstanceProteinSubunitType",
    "SubstanceReferenceInformationType",
    "SubstanceReferenceInformationGeneType",
    "SubstanceReferenceInformationGeneElementType",
    "SubstanceReferenceInformationTargetType",
    "SubstanceSourceMaterialType",
    "SubstanceSourceMaterialFractionDescriptionType",
    "SubstanceSourceMaterialOrganismType",
    "SubstanceSourceMaterialOrganismAuthorType",
    "SubstanceSourceMaterialOrganismHybridType",
    "SubstanceSourceMaterialOrganismOrganismGeneralType",
    "SubstanceSourceMaterialPartDescriptionType",
    "SupplyDeliveryType",
    "SupplyDeliverySuppliedItemType",
    "SupplyRequestType",
    "SupplyRequestParameterType",
    "TaskType",
    "TaskInputType",
    "TaskOutputType",
    "TaskPerformerType",
    "TaskRestrictionType",
    "TerminologyCapabilitiesType",
    "TerminologyCapabilitiesClosureType",
    "TerminologyCapabilitiesCodeSystemType",
    "TerminologyCapabilitiesCodeSystemVersionType",
    "TerminologyCapabilitiesCodeSystemVersionFilterType",
    "TerminologyCapabilitiesExpansionType",
    "TerminologyCapabilitiesExpansionParameterType",
    "TerminologyCapabilitiesImplementationType",
    "TerminologyCapabilitiesSoftwareType",
    "TerminologyCapabilitiesTranslationType",
    "TerminologyCapabilitiesValidateCodeType",
    "TestPlanType",
    "TestPlanDependencyType",
    "TestPlanTestCaseType",
    "TestPlanTestCaseAssertionType",
    "TestPlanTestCaseDependencyType",
    "TestPlanTestCaseTestDataType",
    "TestPlanTestCaseTestRunType",
    "TestPlanTestCaseTestRunScriptType",
    "TestReportType",
    "TestReportParticipantType",
    "TestReportSetupType",
    "TestReportSetupActionType",
    "TestReportSetupActionAssertType",
    "TestReportSetupActionAssertRequirementType",
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
    "TestScriptScopeType",
    "TestScriptSetupType",
    "TestScriptSetupActionType",
    "TestScriptSetupActionAssertType",
    "TestScriptSetupActionAssertRequirementType",
    "TestScriptSetupActionOperationType",
    "TestScriptSetupActionOperationRequestHeaderType",
    "TestScriptTeardownType",
    "TestScriptTeardownActionType",
    "TestScriptTestType",
    "TestScriptTestActionType",
    "TestScriptVariableType",
    "TimingType",
    "TimingRepeatType",
    "TransportType",
    "TransportInputType",
    "TransportOutputType",
    "TransportRestrictionType",
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
    "ValueSetExpansionContainsPropertyType",
    "ValueSetExpansionContainsPropertySubPropertyType",
    "ValueSetExpansionParameterType",
    "ValueSetExpansionPropertyType",
    "ValueSetScopeType",
    "VerificationResultType",
    "VerificationResultAttestationType",
    "VerificationResultPrimarySourceType",
    "VerificationResultValidatorType",
    "VirtualServiceDetailType",
    "VisionPrescriptionType",
    "VisionPrescriptionLensSpecificationType",
    "VisionPrescriptionLensSpecificationPrismType",
]
