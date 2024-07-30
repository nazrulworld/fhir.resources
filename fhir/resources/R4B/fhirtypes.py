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
    "fhir.resources.R4B.fhirprimitiveextension.FHIRPrimitiveExtension",
)

ElementType = create_fhir_element_or_resource_type(
    "ElementType", "fhir.resources.R4B.element.Element"
)

ResourceType = create_fhir_element_or_resource_type(
    "ResourceType", "fhir.resources.R4B.resource.Resource"
)
AccountType = create_fhir_type("AccountType", "fhir.resources.R4B.account.Account")

AccountCoverageType = create_fhir_type(
    "AccountCoverageType", "fhir.resources.R4B.account.AccountCoverage"
)

AccountGuarantorType = create_fhir_type(
    "AccountGuarantorType", "fhir.resources.R4B.account.AccountGuarantor"
)

ActivityDefinitionType = create_fhir_type(
    "ActivityDefinitionType", "fhir.resources.R4B.activitydefinition.ActivityDefinition"
)

ActivityDefinitionDynamicValueType = create_fhir_type(
    "ActivityDefinitionDynamicValueType",
    "fhir.resources.R4B.activitydefinition.ActivityDefinitionDynamicValue",
)

ActivityDefinitionParticipantType = create_fhir_type(
    "ActivityDefinitionParticipantType",
    "fhir.resources.R4B.activitydefinition.ActivityDefinitionParticipant",
)

AddressType = create_fhir_type("AddressType", "fhir.resources.R4B.address.Address")

AdministrableProductDefinitionType = create_fhir_type(
    "AdministrableProductDefinitionType",
    "fhir.resources.R4B.administrableproductdefinition.AdministrableProductDefinition",
)

AdministrableProductDefinitionPropertyType = create_fhir_type(
    "AdministrableProductDefinitionPropertyType",
    "fhir.resources.R4B.administrableproductdefinition.AdministrableProductDefinitionProperty",
)

AdministrableProductDefinitionRouteOfAdministrationType = create_fhir_type(
    "AdministrableProductDefinitionRouteOfAdministrationType",
    "fhir.resources.R4B.administrableproductdefinition.AdministrableProductDefinitionRouteOfAdministration",
)

AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesType = create_fhir_type(
    "AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesType",
    "fhir.resources.R4B.administrableproductdefinition.AdministrableProductDefinitionRouteOfAdministrationTargetSpecies",
)

AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriodType = create_fhir_type(
    "AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriodType",
    "fhir.resources.R4B.administrableproductdefinition.AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod",
)

AdverseEventType = create_fhir_type(
    "AdverseEventType", "fhir.resources.R4B.adverseevent.AdverseEvent"
)

AdverseEventSuspectEntityType = create_fhir_type(
    "AdverseEventSuspectEntityType",
    "fhir.resources.R4B.adverseevent.AdverseEventSuspectEntity",
)

AdverseEventSuspectEntityCausalityType = create_fhir_type(
    "AdverseEventSuspectEntityCausalityType",
    "fhir.resources.R4B.adverseevent.AdverseEventSuspectEntityCausality",
)

AgeType = create_fhir_type("AgeType", "fhir.resources.R4B.age.Age")

AllergyIntoleranceType = create_fhir_type(
    "AllergyIntoleranceType", "fhir.resources.R4B.allergyintolerance.AllergyIntolerance"
)

AllergyIntoleranceReactionType = create_fhir_type(
    "AllergyIntoleranceReactionType",
    "fhir.resources.R4B.allergyintolerance.AllergyIntoleranceReaction",
)

AnnotationType = create_fhir_type(
    "AnnotationType", "fhir.resources.R4B.annotation.Annotation"
)

AppointmentType = create_fhir_type(
    "AppointmentType", "fhir.resources.R4B.appointment.Appointment"
)

AppointmentParticipantType = create_fhir_type(
    "AppointmentParticipantType",
    "fhir.resources.R4B.appointment.AppointmentParticipant",
)

AppointmentResponseType = create_fhir_type(
    "AppointmentResponseType",
    "fhir.resources.R4B.appointmentresponse.AppointmentResponse",
)

AttachmentType = create_fhir_type(
    "AttachmentType", "fhir.resources.R4B.attachment.Attachment"
)

AuditEventType = create_fhir_type(
    "AuditEventType", "fhir.resources.R4B.auditevent.AuditEvent"
)

AuditEventAgentType = create_fhir_type(
    "AuditEventAgentType", "fhir.resources.R4B.auditevent.AuditEventAgent"
)

AuditEventAgentNetworkType = create_fhir_type(
    "AuditEventAgentNetworkType", "fhir.resources.R4B.auditevent.AuditEventAgentNetwork"
)

AuditEventEntityType = create_fhir_type(
    "AuditEventEntityType", "fhir.resources.R4B.auditevent.AuditEventEntity"
)

AuditEventEntityDetailType = create_fhir_type(
    "AuditEventEntityDetailType", "fhir.resources.R4B.auditevent.AuditEventEntityDetail"
)

AuditEventSourceType = create_fhir_type(
    "AuditEventSourceType", "fhir.resources.R4B.auditevent.AuditEventSource"
)

BackboneElementType = create_fhir_type(
    "BackboneElementType", "fhir.resources.R4B.backboneelement.BackboneElement"
)

BasicType = create_fhir_type("BasicType", "fhir.resources.R4B.basic.Basic")

BinaryType = create_fhir_type("BinaryType", "fhir.resources.R4B.binary.Binary")

BiologicallyDerivedProductType = create_fhir_type(
    "BiologicallyDerivedProductType",
    "fhir.resources.R4B.biologicallyderivedproduct.BiologicallyDerivedProduct",
)

BiologicallyDerivedProductCollectionType = create_fhir_type(
    "BiologicallyDerivedProductCollectionType",
    "fhir.resources.R4B.biologicallyderivedproduct.BiologicallyDerivedProductCollection",
)

BiologicallyDerivedProductManipulationType = create_fhir_type(
    "BiologicallyDerivedProductManipulationType",
    "fhir.resources.R4B.biologicallyderivedproduct.BiologicallyDerivedProductManipulation",
)

BiologicallyDerivedProductProcessingType = create_fhir_type(
    "BiologicallyDerivedProductProcessingType",
    "fhir.resources.R4B.biologicallyderivedproduct.BiologicallyDerivedProductProcessing",
)

BiologicallyDerivedProductStorageType = create_fhir_type(
    "BiologicallyDerivedProductStorageType",
    "fhir.resources.R4B.biologicallyderivedproduct.BiologicallyDerivedProductStorage",
)

BodyStructureType = create_fhir_type(
    "BodyStructureType", "fhir.resources.R4B.bodystructure.BodyStructure"
)

BundleType = create_fhir_type("BundleType", "fhir.resources.R4B.bundle.Bundle")

BundleEntryType = create_fhir_type(
    "BundleEntryType", "fhir.resources.R4B.bundle.BundleEntry"
)

BundleEntryRequestType = create_fhir_type(
    "BundleEntryRequestType", "fhir.resources.R4B.bundle.BundleEntryRequest"
)

BundleEntryResponseType = create_fhir_type(
    "BundleEntryResponseType", "fhir.resources.R4B.bundle.BundleEntryResponse"
)

BundleEntrySearchType = create_fhir_type(
    "BundleEntrySearchType", "fhir.resources.R4B.bundle.BundleEntrySearch"
)

BundleLinkType = create_fhir_type(
    "BundleLinkType", "fhir.resources.R4B.bundle.BundleLink"
)

CapabilityStatementType = create_fhir_type(
    "CapabilityStatementType",
    "fhir.resources.R4B.capabilitystatement.CapabilityStatement",
)

CapabilityStatementDocumentType = create_fhir_type(
    "CapabilityStatementDocumentType",
    "fhir.resources.R4B.capabilitystatement.CapabilityStatementDocument",
)

CapabilityStatementImplementationType = create_fhir_type(
    "CapabilityStatementImplementationType",
    "fhir.resources.R4B.capabilitystatement.CapabilityStatementImplementation",
)

CapabilityStatementMessagingType = create_fhir_type(
    "CapabilityStatementMessagingType",
    "fhir.resources.R4B.capabilitystatement.CapabilityStatementMessaging",
)

CapabilityStatementMessagingEndpointType = create_fhir_type(
    "CapabilityStatementMessagingEndpointType",
    "fhir.resources.R4B.capabilitystatement.CapabilityStatementMessagingEndpoint",
)

CapabilityStatementMessagingSupportedMessageType = create_fhir_type(
    "CapabilityStatementMessagingSupportedMessageType",
    "fhir.resources.R4B.capabilitystatement.CapabilityStatementMessagingSupportedMessage",
)

CapabilityStatementRestType = create_fhir_type(
    "CapabilityStatementRestType",
    "fhir.resources.R4B.capabilitystatement.CapabilityStatementRest",
)

CapabilityStatementRestInteractionType = create_fhir_type(
    "CapabilityStatementRestInteractionType",
    "fhir.resources.R4B.capabilitystatement.CapabilityStatementRestInteraction",
)

CapabilityStatementRestResourceType = create_fhir_type(
    "CapabilityStatementRestResourceType",
    "fhir.resources.R4B.capabilitystatement.CapabilityStatementRestResource",
)

CapabilityStatementRestResourceInteractionType = create_fhir_type(
    "CapabilityStatementRestResourceInteractionType",
    "fhir.resources.R4B.capabilitystatement.CapabilityStatementRestResourceInteraction",
)

CapabilityStatementRestResourceOperationType = create_fhir_type(
    "CapabilityStatementRestResourceOperationType",
    "fhir.resources.R4B.capabilitystatement.CapabilityStatementRestResourceOperation",
)

CapabilityStatementRestResourceSearchParamType = create_fhir_type(
    "CapabilityStatementRestResourceSearchParamType",
    "fhir.resources.R4B.capabilitystatement.CapabilityStatementRestResourceSearchParam",
)

CapabilityStatementRestSecurityType = create_fhir_type(
    "CapabilityStatementRestSecurityType",
    "fhir.resources.R4B.capabilitystatement.CapabilityStatementRestSecurity",
)

CapabilityStatementSoftwareType = create_fhir_type(
    "CapabilityStatementSoftwareType",
    "fhir.resources.R4B.capabilitystatement.CapabilityStatementSoftware",
)

CarePlanType = create_fhir_type("CarePlanType", "fhir.resources.R4B.careplan.CarePlan")

CarePlanActivityType = create_fhir_type(
    "CarePlanActivityType", "fhir.resources.R4B.careplan.CarePlanActivity"
)

CarePlanActivityDetailType = create_fhir_type(
    "CarePlanActivityDetailType", "fhir.resources.R4B.careplan.CarePlanActivityDetail"
)

CareTeamType = create_fhir_type("CareTeamType", "fhir.resources.R4B.careteam.CareTeam")

CareTeamParticipantType = create_fhir_type(
    "CareTeamParticipantType", "fhir.resources.R4B.careteam.CareTeamParticipant"
)

CatalogEntryType = create_fhir_type(
    "CatalogEntryType", "fhir.resources.R4B.catalogentry.CatalogEntry"
)

CatalogEntryRelatedEntryType = create_fhir_type(
    "CatalogEntryRelatedEntryType",
    "fhir.resources.R4B.catalogentry.CatalogEntryRelatedEntry",
)

ChargeItemType = create_fhir_type(
    "ChargeItemType", "fhir.resources.R4B.chargeitem.ChargeItem"
)

ChargeItemDefinitionType = create_fhir_type(
    "ChargeItemDefinitionType",
    "fhir.resources.R4B.chargeitemdefinition.ChargeItemDefinition",
)

ChargeItemDefinitionApplicabilityType = create_fhir_type(
    "ChargeItemDefinitionApplicabilityType",
    "fhir.resources.R4B.chargeitemdefinition.ChargeItemDefinitionApplicability",
)

ChargeItemDefinitionPropertyGroupType = create_fhir_type(
    "ChargeItemDefinitionPropertyGroupType",
    "fhir.resources.R4B.chargeitemdefinition.ChargeItemDefinitionPropertyGroup",
)

ChargeItemDefinitionPropertyGroupPriceComponentType = create_fhir_type(
    "ChargeItemDefinitionPropertyGroupPriceComponentType",
    "fhir.resources.R4B.chargeitemdefinition.ChargeItemDefinitionPropertyGroupPriceComponent",
)

ChargeItemPerformerType = create_fhir_type(
    "ChargeItemPerformerType", "fhir.resources.R4B.chargeitem.ChargeItemPerformer"
)

CitationType = create_fhir_type("CitationType", "fhir.resources.R4B.citation.Citation")

CitationCitedArtifactType = create_fhir_type(
    "CitationCitedArtifactType", "fhir.resources.R4B.citation.CitationCitedArtifact"
)

CitationCitedArtifactAbstractType = create_fhir_type(
    "CitationCitedArtifactAbstractType",
    "fhir.resources.R4B.citation.CitationCitedArtifactAbstract",
)

CitationCitedArtifactClassificationType = create_fhir_type(
    "CitationCitedArtifactClassificationType",
    "fhir.resources.R4B.citation.CitationCitedArtifactClassification",
)

CitationCitedArtifactClassificationWhoClassifiedType = create_fhir_type(
    "CitationCitedArtifactClassificationWhoClassifiedType",
    "fhir.resources.R4B.citation.CitationCitedArtifactClassificationWhoClassified",
)

CitationCitedArtifactContributorshipType = create_fhir_type(
    "CitationCitedArtifactContributorshipType",
    "fhir.resources.R4B.citation.CitationCitedArtifactContributorship",
)

CitationCitedArtifactContributorshipEntryType = create_fhir_type(
    "CitationCitedArtifactContributorshipEntryType",
    "fhir.resources.R4B.citation.CitationCitedArtifactContributorshipEntry",
)

CitationCitedArtifactContributorshipEntryAffiliationInfoType = create_fhir_type(
    "CitationCitedArtifactContributorshipEntryAffiliationInfoType",
    "fhir.resources.R4B.citation.CitationCitedArtifactContributorshipEntryAffiliationInfo",
)

CitationCitedArtifactContributorshipEntryContributionInstanceType = create_fhir_type(
    "CitationCitedArtifactContributorshipEntryContributionInstanceType",
    "fhir.resources.R4B.citation.CitationCitedArtifactContributorshipEntryContributionInstance",
)

CitationCitedArtifactContributorshipSummaryType = create_fhir_type(
    "CitationCitedArtifactContributorshipSummaryType",
    "fhir.resources.R4B.citation.CitationCitedArtifactContributorshipSummary",
)

CitationCitedArtifactPartType = create_fhir_type(
    "CitationCitedArtifactPartType",
    "fhir.resources.R4B.citation.CitationCitedArtifactPart",
)

CitationCitedArtifactPublicationFormType = create_fhir_type(
    "CitationCitedArtifactPublicationFormType",
    "fhir.resources.R4B.citation.CitationCitedArtifactPublicationForm",
)

CitationCitedArtifactPublicationFormPeriodicReleaseType = create_fhir_type(
    "CitationCitedArtifactPublicationFormPeriodicReleaseType",
    "fhir.resources.R4B.citation.CitationCitedArtifactPublicationFormPeriodicRelease",
)

CitationCitedArtifactPublicationFormPeriodicReleaseDateOfPublicationType = create_fhir_type(
    "CitationCitedArtifactPublicationFormPeriodicReleaseDateOfPublicationType",
    "fhir.resources.R4B.citation.CitationCitedArtifactPublicationFormPeriodicReleaseDateOfPublication",
)

CitationCitedArtifactPublicationFormPublishedInType = create_fhir_type(
    "CitationCitedArtifactPublicationFormPublishedInType",
    "fhir.resources.R4B.citation.CitationCitedArtifactPublicationFormPublishedIn",
)

CitationCitedArtifactRelatesToType = create_fhir_type(
    "CitationCitedArtifactRelatesToType",
    "fhir.resources.R4B.citation.CitationCitedArtifactRelatesTo",
)

CitationCitedArtifactStatusDateType = create_fhir_type(
    "CitationCitedArtifactStatusDateType",
    "fhir.resources.R4B.citation.CitationCitedArtifactStatusDate",
)

CitationCitedArtifactTitleType = create_fhir_type(
    "CitationCitedArtifactTitleType",
    "fhir.resources.R4B.citation.CitationCitedArtifactTitle",
)

CitationCitedArtifactVersionType = create_fhir_type(
    "CitationCitedArtifactVersionType",
    "fhir.resources.R4B.citation.CitationCitedArtifactVersion",
)

CitationCitedArtifactWebLocationType = create_fhir_type(
    "CitationCitedArtifactWebLocationType",
    "fhir.resources.R4B.citation.CitationCitedArtifactWebLocation",
)

CitationClassificationType = create_fhir_type(
    "CitationClassificationType", "fhir.resources.R4B.citation.CitationClassification"
)

CitationRelatesToType = create_fhir_type(
    "CitationRelatesToType", "fhir.resources.R4B.citation.CitationRelatesTo"
)

CitationStatusDateType = create_fhir_type(
    "CitationStatusDateType", "fhir.resources.R4B.citation.CitationStatusDate"
)

CitationSummaryType = create_fhir_type(
    "CitationSummaryType", "fhir.resources.R4B.citation.CitationSummary"
)

ClaimType = create_fhir_type("ClaimType", "fhir.resources.R4B.claim.Claim")

ClaimAccidentType = create_fhir_type(
    "ClaimAccidentType", "fhir.resources.R4B.claim.ClaimAccident"
)

ClaimCareTeamType = create_fhir_type(
    "ClaimCareTeamType", "fhir.resources.R4B.claim.ClaimCareTeam"
)

ClaimDiagnosisType = create_fhir_type(
    "ClaimDiagnosisType", "fhir.resources.R4B.claim.ClaimDiagnosis"
)

ClaimInsuranceType = create_fhir_type(
    "ClaimInsuranceType", "fhir.resources.R4B.claim.ClaimInsurance"
)

ClaimItemType = create_fhir_type("ClaimItemType", "fhir.resources.R4B.claim.ClaimItem")

ClaimItemDetailType = create_fhir_type(
    "ClaimItemDetailType", "fhir.resources.R4B.claim.ClaimItemDetail"
)

ClaimItemDetailSubDetailType = create_fhir_type(
    "ClaimItemDetailSubDetailType", "fhir.resources.R4B.claim.ClaimItemDetailSubDetail"
)

ClaimPayeeType = create_fhir_type(
    "ClaimPayeeType", "fhir.resources.R4B.claim.ClaimPayee"
)

ClaimProcedureType = create_fhir_type(
    "ClaimProcedureType", "fhir.resources.R4B.claim.ClaimProcedure"
)

ClaimRelatedType = create_fhir_type(
    "ClaimRelatedType", "fhir.resources.R4B.claim.ClaimRelated"
)

ClaimResponseType = create_fhir_type(
    "ClaimResponseType", "fhir.resources.R4B.claimresponse.ClaimResponse"
)

ClaimResponseAddItemType = create_fhir_type(
    "ClaimResponseAddItemType", "fhir.resources.R4B.claimresponse.ClaimResponseAddItem"
)

ClaimResponseAddItemDetailType = create_fhir_type(
    "ClaimResponseAddItemDetailType",
    "fhir.resources.R4B.claimresponse.ClaimResponseAddItemDetail",
)

ClaimResponseAddItemDetailSubDetailType = create_fhir_type(
    "ClaimResponseAddItemDetailSubDetailType",
    "fhir.resources.R4B.claimresponse.ClaimResponseAddItemDetailSubDetail",
)

ClaimResponseErrorType = create_fhir_type(
    "ClaimResponseErrorType", "fhir.resources.R4B.claimresponse.ClaimResponseError"
)

ClaimResponseInsuranceType = create_fhir_type(
    "ClaimResponseInsuranceType",
    "fhir.resources.R4B.claimresponse.ClaimResponseInsurance",
)

ClaimResponseItemType = create_fhir_type(
    "ClaimResponseItemType", "fhir.resources.R4B.claimresponse.ClaimResponseItem"
)

ClaimResponseItemAdjudicationType = create_fhir_type(
    "ClaimResponseItemAdjudicationType",
    "fhir.resources.R4B.claimresponse.ClaimResponseItemAdjudication",
)

ClaimResponseItemDetailType = create_fhir_type(
    "ClaimResponseItemDetailType",
    "fhir.resources.R4B.claimresponse.ClaimResponseItemDetail",
)

ClaimResponseItemDetailSubDetailType = create_fhir_type(
    "ClaimResponseItemDetailSubDetailType",
    "fhir.resources.R4B.claimresponse.ClaimResponseItemDetailSubDetail",
)

ClaimResponsePaymentType = create_fhir_type(
    "ClaimResponsePaymentType", "fhir.resources.R4B.claimresponse.ClaimResponsePayment"
)

ClaimResponseProcessNoteType = create_fhir_type(
    "ClaimResponseProcessNoteType",
    "fhir.resources.R4B.claimresponse.ClaimResponseProcessNote",
)

ClaimResponseTotalType = create_fhir_type(
    "ClaimResponseTotalType", "fhir.resources.R4B.claimresponse.ClaimResponseTotal"
)

ClaimSupportingInfoType = create_fhir_type(
    "ClaimSupportingInfoType", "fhir.resources.R4B.claim.ClaimSupportingInfo"
)

ClinicalImpressionType = create_fhir_type(
    "ClinicalImpressionType", "fhir.resources.R4B.clinicalimpression.ClinicalImpression"
)

ClinicalImpressionFindingType = create_fhir_type(
    "ClinicalImpressionFindingType",
    "fhir.resources.R4B.clinicalimpression.ClinicalImpressionFinding",
)

ClinicalImpressionInvestigationType = create_fhir_type(
    "ClinicalImpressionInvestigationType",
    "fhir.resources.R4B.clinicalimpression.ClinicalImpressionInvestigation",
)

ClinicalUseDefinitionType = create_fhir_type(
    "ClinicalUseDefinitionType",
    "fhir.resources.R4B.clinicalusedefinition.ClinicalUseDefinition",
)

ClinicalUseDefinitionContraindicationType = create_fhir_type(
    "ClinicalUseDefinitionContraindicationType",
    "fhir.resources.R4B.clinicalusedefinition.ClinicalUseDefinitionContraindication",
)

ClinicalUseDefinitionContraindicationOtherTherapyType = create_fhir_type(
    "ClinicalUseDefinitionContraindicationOtherTherapyType",
    "fhir.resources.R4B.clinicalusedefinition.ClinicalUseDefinitionContraindicationOtherTherapy",
)

ClinicalUseDefinitionIndicationType = create_fhir_type(
    "ClinicalUseDefinitionIndicationType",
    "fhir.resources.R4B.clinicalusedefinition.ClinicalUseDefinitionIndication",
)

ClinicalUseDefinitionInteractionType = create_fhir_type(
    "ClinicalUseDefinitionInteractionType",
    "fhir.resources.R4B.clinicalusedefinition.ClinicalUseDefinitionInteraction",
)

ClinicalUseDefinitionInteractionInteractantType = create_fhir_type(
    "ClinicalUseDefinitionInteractionInteractantType",
    "fhir.resources.R4B.clinicalusedefinition.ClinicalUseDefinitionInteractionInteractant",
)

ClinicalUseDefinitionUndesirableEffectType = create_fhir_type(
    "ClinicalUseDefinitionUndesirableEffectType",
    "fhir.resources.R4B.clinicalusedefinition.ClinicalUseDefinitionUndesirableEffect",
)

ClinicalUseDefinitionWarningType = create_fhir_type(
    "ClinicalUseDefinitionWarningType",
    "fhir.resources.R4B.clinicalusedefinition.ClinicalUseDefinitionWarning",
)

CodeSystemType = create_fhir_type(
    "CodeSystemType", "fhir.resources.R4B.codesystem.CodeSystem"
)

CodeSystemConceptType = create_fhir_type(
    "CodeSystemConceptType", "fhir.resources.R4B.codesystem.CodeSystemConcept"
)

CodeSystemConceptDesignationType = create_fhir_type(
    "CodeSystemConceptDesignationType",
    "fhir.resources.R4B.codesystem.CodeSystemConceptDesignation",
)

CodeSystemConceptPropertyType = create_fhir_type(
    "CodeSystemConceptPropertyType",
    "fhir.resources.R4B.codesystem.CodeSystemConceptProperty",
)

CodeSystemFilterType = create_fhir_type(
    "CodeSystemFilterType", "fhir.resources.R4B.codesystem.CodeSystemFilter"
)

CodeSystemPropertyType = create_fhir_type(
    "CodeSystemPropertyType", "fhir.resources.R4B.codesystem.CodeSystemProperty"
)

CodeableConceptType = create_fhir_type(
    "CodeableConceptType", "fhir.resources.R4B.codeableconcept.CodeableConcept"
)

CodeableReferenceType = create_fhir_type(
    "CodeableReferenceType", "fhir.resources.R4B.codeablereference.CodeableReference"
)

CodingType = create_fhir_type("CodingType", "fhir.resources.R4B.coding.Coding")

CommunicationType = create_fhir_type(
    "CommunicationType", "fhir.resources.R4B.communication.Communication"
)

CommunicationPayloadType = create_fhir_type(
    "CommunicationPayloadType", "fhir.resources.R4B.communication.CommunicationPayload"
)

CommunicationRequestType = create_fhir_type(
    "CommunicationRequestType",
    "fhir.resources.R4B.communicationrequest.CommunicationRequest",
)

CommunicationRequestPayloadType = create_fhir_type(
    "CommunicationRequestPayloadType",
    "fhir.resources.R4B.communicationrequest.CommunicationRequestPayload",
)

CompartmentDefinitionType = create_fhir_type(
    "CompartmentDefinitionType",
    "fhir.resources.R4B.compartmentdefinition.CompartmentDefinition",
)

CompartmentDefinitionResourceType = create_fhir_type(
    "CompartmentDefinitionResourceType",
    "fhir.resources.R4B.compartmentdefinition.CompartmentDefinitionResource",
)

CompositionType = create_fhir_type(
    "CompositionType", "fhir.resources.R4B.composition.Composition"
)

CompositionAttesterType = create_fhir_type(
    "CompositionAttesterType", "fhir.resources.R4B.composition.CompositionAttester"
)

CompositionEventType = create_fhir_type(
    "CompositionEventType", "fhir.resources.R4B.composition.CompositionEvent"
)

CompositionRelatesToType = create_fhir_type(
    "CompositionRelatesToType", "fhir.resources.R4B.composition.CompositionRelatesTo"
)

CompositionSectionType = create_fhir_type(
    "CompositionSectionType", "fhir.resources.R4B.composition.CompositionSection"
)

ConceptMapType = create_fhir_type(
    "ConceptMapType", "fhir.resources.R4B.conceptmap.ConceptMap"
)

ConceptMapGroupType = create_fhir_type(
    "ConceptMapGroupType", "fhir.resources.R4B.conceptmap.ConceptMapGroup"
)

ConceptMapGroupElementType = create_fhir_type(
    "ConceptMapGroupElementType", "fhir.resources.R4B.conceptmap.ConceptMapGroupElement"
)

ConceptMapGroupElementTargetType = create_fhir_type(
    "ConceptMapGroupElementTargetType",
    "fhir.resources.R4B.conceptmap.ConceptMapGroupElementTarget",
)

ConceptMapGroupElementTargetDependsOnType = create_fhir_type(
    "ConceptMapGroupElementTargetDependsOnType",
    "fhir.resources.R4B.conceptmap.ConceptMapGroupElementTargetDependsOn",
)

ConceptMapGroupUnmappedType = create_fhir_type(
    "ConceptMapGroupUnmappedType",
    "fhir.resources.R4B.conceptmap.ConceptMapGroupUnmapped",
)

ConditionType = create_fhir_type(
    "ConditionType", "fhir.resources.R4B.condition.Condition"
)

ConditionEvidenceType = create_fhir_type(
    "ConditionEvidenceType", "fhir.resources.R4B.condition.ConditionEvidence"
)

ConditionStageType = create_fhir_type(
    "ConditionStageType", "fhir.resources.R4B.condition.ConditionStage"
)

ConsentType = create_fhir_type("ConsentType", "fhir.resources.R4B.consent.Consent")

ConsentPolicyType = create_fhir_type(
    "ConsentPolicyType", "fhir.resources.R4B.consent.ConsentPolicy"
)

ConsentProvisionType = create_fhir_type(
    "ConsentProvisionType", "fhir.resources.R4B.consent.ConsentProvision"
)

ConsentProvisionActorType = create_fhir_type(
    "ConsentProvisionActorType", "fhir.resources.R4B.consent.ConsentProvisionActor"
)

ConsentProvisionDataType = create_fhir_type(
    "ConsentProvisionDataType", "fhir.resources.R4B.consent.ConsentProvisionData"
)

ConsentVerificationType = create_fhir_type(
    "ConsentVerificationType", "fhir.resources.R4B.consent.ConsentVerification"
)

ContactDetailType = create_fhir_type(
    "ContactDetailType", "fhir.resources.R4B.contactdetail.ContactDetail"
)

ContactPointType = create_fhir_type(
    "ContactPointType", "fhir.resources.R4B.contactpoint.ContactPoint"
)

ContractType = create_fhir_type("ContractType", "fhir.resources.R4B.contract.Contract")

ContractContentDefinitionType = create_fhir_type(
    "ContractContentDefinitionType",
    "fhir.resources.R4B.contract.ContractContentDefinition",
)

ContractFriendlyType = create_fhir_type(
    "ContractFriendlyType", "fhir.resources.R4B.contract.ContractFriendly"
)

ContractLegalType = create_fhir_type(
    "ContractLegalType", "fhir.resources.R4B.contract.ContractLegal"
)

ContractRuleType = create_fhir_type(
    "ContractRuleType", "fhir.resources.R4B.contract.ContractRule"
)

ContractSignerType = create_fhir_type(
    "ContractSignerType", "fhir.resources.R4B.contract.ContractSigner"
)

ContractTermType = create_fhir_type(
    "ContractTermType", "fhir.resources.R4B.contract.ContractTerm"
)

ContractTermActionType = create_fhir_type(
    "ContractTermActionType", "fhir.resources.R4B.contract.ContractTermAction"
)

ContractTermActionSubjectType = create_fhir_type(
    "ContractTermActionSubjectType",
    "fhir.resources.R4B.contract.ContractTermActionSubject",
)

ContractTermAssetType = create_fhir_type(
    "ContractTermAssetType", "fhir.resources.R4B.contract.ContractTermAsset"
)

ContractTermAssetContextType = create_fhir_type(
    "ContractTermAssetContextType",
    "fhir.resources.R4B.contract.ContractTermAssetContext",
)

ContractTermAssetValuedItemType = create_fhir_type(
    "ContractTermAssetValuedItemType",
    "fhir.resources.R4B.contract.ContractTermAssetValuedItem",
)

ContractTermOfferType = create_fhir_type(
    "ContractTermOfferType", "fhir.resources.R4B.contract.ContractTermOffer"
)

ContractTermOfferAnswerType = create_fhir_type(
    "ContractTermOfferAnswerType", "fhir.resources.R4B.contract.ContractTermOfferAnswer"
)

ContractTermOfferPartyType = create_fhir_type(
    "ContractTermOfferPartyType", "fhir.resources.R4B.contract.ContractTermOfferParty"
)

ContractTermSecurityLabelType = create_fhir_type(
    "ContractTermSecurityLabelType",
    "fhir.resources.R4B.contract.ContractTermSecurityLabel",
)

ContributorType = create_fhir_type(
    "ContributorType", "fhir.resources.R4B.contributor.Contributor"
)

CountType = create_fhir_type("CountType", "fhir.resources.R4B.count.Count")

CoverageType = create_fhir_type("CoverageType", "fhir.resources.R4B.coverage.Coverage")

CoverageClassType = create_fhir_type(
    "CoverageClassType", "fhir.resources.R4B.coverage.CoverageClass"
)

CoverageCostToBeneficiaryType = create_fhir_type(
    "CoverageCostToBeneficiaryType",
    "fhir.resources.R4B.coverage.CoverageCostToBeneficiary",
)

CoverageCostToBeneficiaryExceptionType = create_fhir_type(
    "CoverageCostToBeneficiaryExceptionType",
    "fhir.resources.R4B.coverage.CoverageCostToBeneficiaryException",
)

CoverageEligibilityRequestType = create_fhir_type(
    "CoverageEligibilityRequestType",
    "fhir.resources.R4B.coverageeligibilityrequest.CoverageEligibilityRequest",
)

CoverageEligibilityRequestInsuranceType = create_fhir_type(
    "CoverageEligibilityRequestInsuranceType",
    "fhir.resources.R4B.coverageeligibilityrequest.CoverageEligibilityRequestInsurance",
)

CoverageEligibilityRequestItemType = create_fhir_type(
    "CoverageEligibilityRequestItemType",
    "fhir.resources.R4B.coverageeligibilityrequest.CoverageEligibilityRequestItem",
)

CoverageEligibilityRequestItemDiagnosisType = create_fhir_type(
    "CoverageEligibilityRequestItemDiagnosisType",
    "fhir.resources.R4B.coverageeligibilityrequest.CoverageEligibilityRequestItemDiagnosis",
)

CoverageEligibilityRequestSupportingInfoType = create_fhir_type(
    "CoverageEligibilityRequestSupportingInfoType",
    "fhir.resources.R4B.coverageeligibilityrequest.CoverageEligibilityRequestSupportingInfo",
)

CoverageEligibilityResponseType = create_fhir_type(
    "CoverageEligibilityResponseType",
    "fhir.resources.R4B.coverageeligibilityresponse.CoverageEligibilityResponse",
)

CoverageEligibilityResponseErrorType = create_fhir_type(
    "CoverageEligibilityResponseErrorType",
    "fhir.resources.R4B.coverageeligibilityresponse.CoverageEligibilityResponseError",
)

CoverageEligibilityResponseInsuranceType = create_fhir_type(
    "CoverageEligibilityResponseInsuranceType",
    "fhir.resources.R4B.coverageeligibilityresponse.CoverageEligibilityResponseInsurance",
)

CoverageEligibilityResponseInsuranceItemType = create_fhir_type(
    "CoverageEligibilityResponseInsuranceItemType",
    "fhir.resources.R4B.coverageeligibilityresponse.CoverageEligibilityResponseInsuranceItem",
)

CoverageEligibilityResponseInsuranceItemBenefitType = create_fhir_type(
    "CoverageEligibilityResponseInsuranceItemBenefitType",
    "fhir.resources.R4B.coverageeligibilityresponse.CoverageEligibilityResponseInsuranceItemBenefit",
)

DataRequirementType = create_fhir_type(
    "DataRequirementType", "fhir.resources.R4B.datarequirement.DataRequirement"
)

DataRequirementCodeFilterType = create_fhir_type(
    "DataRequirementCodeFilterType",
    "fhir.resources.R4B.datarequirement.DataRequirementCodeFilter",
)

DataRequirementDateFilterType = create_fhir_type(
    "DataRequirementDateFilterType",
    "fhir.resources.R4B.datarequirement.DataRequirementDateFilter",
)

DataRequirementSortType = create_fhir_type(
    "DataRequirementSortType", "fhir.resources.R4B.datarequirement.DataRequirementSort"
)

DetectedIssueType = create_fhir_type(
    "DetectedIssueType", "fhir.resources.R4B.detectedissue.DetectedIssue"
)

DetectedIssueEvidenceType = create_fhir_type(
    "DetectedIssueEvidenceType",
    "fhir.resources.R4B.detectedissue.DetectedIssueEvidence",
)

DetectedIssueMitigationType = create_fhir_type(
    "DetectedIssueMitigationType",
    "fhir.resources.R4B.detectedissue.DetectedIssueMitigation",
)

DeviceType = create_fhir_type("DeviceType", "fhir.resources.R4B.device.Device")

DeviceDefinitionType = create_fhir_type(
    "DeviceDefinitionType", "fhir.resources.R4B.devicedefinition.DeviceDefinition"
)

DeviceDefinitionCapabilityType = create_fhir_type(
    "DeviceDefinitionCapabilityType",
    "fhir.resources.R4B.devicedefinition.DeviceDefinitionCapability",
)

DeviceDefinitionDeviceNameType = create_fhir_type(
    "DeviceDefinitionDeviceNameType",
    "fhir.resources.R4B.devicedefinition.DeviceDefinitionDeviceName",
)

DeviceDefinitionMaterialType = create_fhir_type(
    "DeviceDefinitionMaterialType",
    "fhir.resources.R4B.devicedefinition.DeviceDefinitionMaterial",
)

DeviceDefinitionPropertyType = create_fhir_type(
    "DeviceDefinitionPropertyType",
    "fhir.resources.R4B.devicedefinition.DeviceDefinitionProperty",
)

DeviceDefinitionSpecializationType = create_fhir_type(
    "DeviceDefinitionSpecializationType",
    "fhir.resources.R4B.devicedefinition.DeviceDefinitionSpecialization",
)

DeviceDefinitionUdiDeviceIdentifierType = create_fhir_type(
    "DeviceDefinitionUdiDeviceIdentifierType",
    "fhir.resources.R4B.devicedefinition.DeviceDefinitionUdiDeviceIdentifier",
)

DeviceDeviceNameType = create_fhir_type(
    "DeviceDeviceNameType", "fhir.resources.R4B.device.DeviceDeviceName"
)

DeviceMetricType = create_fhir_type(
    "DeviceMetricType", "fhir.resources.R4B.devicemetric.DeviceMetric"
)

DeviceMetricCalibrationType = create_fhir_type(
    "DeviceMetricCalibrationType",
    "fhir.resources.R4B.devicemetric.DeviceMetricCalibration",
)

DevicePropertyType = create_fhir_type(
    "DevicePropertyType", "fhir.resources.R4B.device.DeviceProperty"
)

DeviceRequestType = create_fhir_type(
    "DeviceRequestType", "fhir.resources.R4B.devicerequest.DeviceRequest"
)

DeviceRequestParameterType = create_fhir_type(
    "DeviceRequestParameterType",
    "fhir.resources.R4B.devicerequest.DeviceRequestParameter",
)

DeviceSpecializationType = create_fhir_type(
    "DeviceSpecializationType", "fhir.resources.R4B.device.DeviceSpecialization"
)

DeviceUdiCarrierType = create_fhir_type(
    "DeviceUdiCarrierType", "fhir.resources.R4B.device.DeviceUdiCarrier"
)

DeviceUseStatementType = create_fhir_type(
    "DeviceUseStatementType", "fhir.resources.R4B.deviceusestatement.DeviceUseStatement"
)

DeviceVersionType = create_fhir_type(
    "DeviceVersionType", "fhir.resources.R4B.device.DeviceVersion"
)

DiagnosticReportType = create_fhir_type(
    "DiagnosticReportType", "fhir.resources.R4B.diagnosticreport.DiagnosticReport"
)

DiagnosticReportMediaType = create_fhir_type(
    "DiagnosticReportMediaType",
    "fhir.resources.R4B.diagnosticreport.DiagnosticReportMedia",
)

DistanceType = create_fhir_type("DistanceType", "fhir.resources.R4B.distance.Distance")

DocumentManifestType = create_fhir_type(
    "DocumentManifestType", "fhir.resources.R4B.documentmanifest.DocumentManifest"
)

DocumentManifestRelatedType = create_fhir_type(
    "DocumentManifestRelatedType",
    "fhir.resources.R4B.documentmanifest.DocumentManifestRelated",
)

DocumentReferenceType = create_fhir_type(
    "DocumentReferenceType", "fhir.resources.R4B.documentreference.DocumentReference"
)

DocumentReferenceContentType = create_fhir_type(
    "DocumentReferenceContentType",
    "fhir.resources.R4B.documentreference.DocumentReferenceContent",
)

DocumentReferenceContextType = create_fhir_type(
    "DocumentReferenceContextType",
    "fhir.resources.R4B.documentreference.DocumentReferenceContext",
)

DocumentReferenceRelatesToType = create_fhir_type(
    "DocumentReferenceRelatesToType",
    "fhir.resources.R4B.documentreference.DocumentReferenceRelatesTo",
)

DomainResourceType = create_fhir_type(
    "DomainResourceType", "fhir.resources.R4B.domainresource.DomainResource"
)

DosageType = create_fhir_type("DosageType", "fhir.resources.R4B.dosage.Dosage")

DosageDoseAndRateType = create_fhir_type(
    "DosageDoseAndRateType", "fhir.resources.R4B.dosage.DosageDoseAndRate"
)

DurationType = create_fhir_type("DurationType", "fhir.resources.R4B.duration.Duration")

ElementDefinitionType = create_fhir_type(
    "ElementDefinitionType", "fhir.resources.R4B.elementdefinition.ElementDefinition"
)

ElementDefinitionBaseType = create_fhir_type(
    "ElementDefinitionBaseType",
    "fhir.resources.R4B.elementdefinition.ElementDefinitionBase",
)

ElementDefinitionBindingType = create_fhir_type(
    "ElementDefinitionBindingType",
    "fhir.resources.R4B.elementdefinition.ElementDefinitionBinding",
)

ElementDefinitionConstraintType = create_fhir_type(
    "ElementDefinitionConstraintType",
    "fhir.resources.R4B.elementdefinition.ElementDefinitionConstraint",
)

ElementDefinitionExampleType = create_fhir_type(
    "ElementDefinitionExampleType",
    "fhir.resources.R4B.elementdefinition.ElementDefinitionExample",
)

ElementDefinitionMappingType = create_fhir_type(
    "ElementDefinitionMappingType",
    "fhir.resources.R4B.elementdefinition.ElementDefinitionMapping",
)

ElementDefinitionSlicingType = create_fhir_type(
    "ElementDefinitionSlicingType",
    "fhir.resources.R4B.elementdefinition.ElementDefinitionSlicing",
)

ElementDefinitionSlicingDiscriminatorType = create_fhir_type(
    "ElementDefinitionSlicingDiscriminatorType",
    "fhir.resources.R4B.elementdefinition.ElementDefinitionSlicingDiscriminator",
)

ElementDefinitionTypeType = create_fhir_type(
    "ElementDefinitionTypeType",
    "fhir.resources.R4B.elementdefinition.ElementDefinitionType",
)

EncounterType = create_fhir_type(
    "EncounterType", "fhir.resources.R4B.encounter.Encounter"
)

EncounterClassHistoryType = create_fhir_type(
    "EncounterClassHistoryType", "fhir.resources.R4B.encounter.EncounterClassHistory"
)

EncounterDiagnosisType = create_fhir_type(
    "EncounterDiagnosisType", "fhir.resources.R4B.encounter.EncounterDiagnosis"
)

EncounterHospitalizationType = create_fhir_type(
    "EncounterHospitalizationType",
    "fhir.resources.R4B.encounter.EncounterHospitalization",
)

EncounterLocationType = create_fhir_type(
    "EncounterLocationType", "fhir.resources.R4B.encounter.EncounterLocation"
)

EncounterParticipantType = create_fhir_type(
    "EncounterParticipantType", "fhir.resources.R4B.encounter.EncounterParticipant"
)

EncounterStatusHistoryType = create_fhir_type(
    "EncounterStatusHistoryType", "fhir.resources.R4B.encounter.EncounterStatusHistory"
)

EndpointType = create_fhir_type("EndpointType", "fhir.resources.R4B.endpoint.Endpoint")

EnrollmentRequestType = create_fhir_type(
    "EnrollmentRequestType", "fhir.resources.R4B.enrollmentrequest.EnrollmentRequest"
)

EnrollmentResponseType = create_fhir_type(
    "EnrollmentResponseType", "fhir.resources.R4B.enrollmentresponse.EnrollmentResponse"
)

EpisodeOfCareType = create_fhir_type(
    "EpisodeOfCareType", "fhir.resources.R4B.episodeofcare.EpisodeOfCare"
)

EpisodeOfCareDiagnosisType = create_fhir_type(
    "EpisodeOfCareDiagnosisType",
    "fhir.resources.R4B.episodeofcare.EpisodeOfCareDiagnosis",
)

EpisodeOfCareStatusHistoryType = create_fhir_type(
    "EpisodeOfCareStatusHistoryType",
    "fhir.resources.R4B.episodeofcare.EpisodeOfCareStatusHistory",
)

EventDefinitionType = create_fhir_type(
    "EventDefinitionType", "fhir.resources.R4B.eventdefinition.EventDefinition"
)

EvidenceType = create_fhir_type("EvidenceType", "fhir.resources.R4B.evidence.Evidence")

EvidenceCertaintyType = create_fhir_type(
    "EvidenceCertaintyType", "fhir.resources.R4B.evidence.EvidenceCertainty"
)

EvidenceReportType = create_fhir_type(
    "EvidenceReportType", "fhir.resources.R4B.evidencereport.EvidenceReport"
)

EvidenceReportRelatesToType = create_fhir_type(
    "EvidenceReportRelatesToType",
    "fhir.resources.R4B.evidencereport.EvidenceReportRelatesTo",
)

EvidenceReportSectionType = create_fhir_type(
    "EvidenceReportSectionType",
    "fhir.resources.R4B.evidencereport.EvidenceReportSection",
)

EvidenceReportSubjectType = create_fhir_type(
    "EvidenceReportSubjectType",
    "fhir.resources.R4B.evidencereport.EvidenceReportSubject",
)

EvidenceReportSubjectCharacteristicType = create_fhir_type(
    "EvidenceReportSubjectCharacteristicType",
    "fhir.resources.R4B.evidencereport.EvidenceReportSubjectCharacteristic",
)

EvidenceStatisticType = create_fhir_type(
    "EvidenceStatisticType", "fhir.resources.R4B.evidence.EvidenceStatistic"
)

EvidenceStatisticAttributeEstimateType = create_fhir_type(
    "EvidenceStatisticAttributeEstimateType",
    "fhir.resources.R4B.evidence.EvidenceStatisticAttributeEstimate",
)

EvidenceStatisticModelCharacteristicType = create_fhir_type(
    "EvidenceStatisticModelCharacteristicType",
    "fhir.resources.R4B.evidence.EvidenceStatisticModelCharacteristic",
)

EvidenceStatisticModelCharacteristicVariableType = create_fhir_type(
    "EvidenceStatisticModelCharacteristicVariableType",
    "fhir.resources.R4B.evidence.EvidenceStatisticModelCharacteristicVariable",
)

EvidenceStatisticSampleSizeType = create_fhir_type(
    "EvidenceStatisticSampleSizeType",
    "fhir.resources.R4B.evidence.EvidenceStatisticSampleSize",
)

EvidenceVariableType = create_fhir_type(
    "EvidenceVariableType", "fhir.resources.R4B.evidencevariable.EvidenceVariable"
)

EvidenceVariableCategoryType = create_fhir_type(
    "EvidenceVariableCategoryType",
    "fhir.resources.R4B.evidencevariable.EvidenceVariableCategory",
)

EvidenceVariableCharacteristicType = create_fhir_type(
    "EvidenceVariableCharacteristicType",
    "fhir.resources.R4B.evidencevariable.EvidenceVariableCharacteristic",
)

EvidenceVariableCharacteristicTimeFromStartType = create_fhir_type(
    "EvidenceVariableCharacteristicTimeFromStartType",
    "fhir.resources.R4B.evidencevariable.EvidenceVariableCharacteristicTimeFromStart",
)

EvidenceVariableDefinitionType = create_fhir_type(
    "EvidenceVariableDefinitionType",
    "fhir.resources.R4B.evidence.EvidenceVariableDefinition",
)

ExampleScenarioType = create_fhir_type(
    "ExampleScenarioType", "fhir.resources.R4B.examplescenario.ExampleScenario"
)

ExampleScenarioActorType = create_fhir_type(
    "ExampleScenarioActorType",
    "fhir.resources.R4B.examplescenario.ExampleScenarioActor",
)

ExampleScenarioInstanceType = create_fhir_type(
    "ExampleScenarioInstanceType",
    "fhir.resources.R4B.examplescenario.ExampleScenarioInstance",
)

ExampleScenarioInstanceContainedInstanceType = create_fhir_type(
    "ExampleScenarioInstanceContainedInstanceType",
    "fhir.resources.R4B.examplescenario.ExampleScenarioInstanceContainedInstance",
)

ExampleScenarioInstanceVersionType = create_fhir_type(
    "ExampleScenarioInstanceVersionType",
    "fhir.resources.R4B.examplescenario.ExampleScenarioInstanceVersion",
)

ExampleScenarioProcessType = create_fhir_type(
    "ExampleScenarioProcessType",
    "fhir.resources.R4B.examplescenario.ExampleScenarioProcess",
)

ExampleScenarioProcessStepType = create_fhir_type(
    "ExampleScenarioProcessStepType",
    "fhir.resources.R4B.examplescenario.ExampleScenarioProcessStep",
)

ExampleScenarioProcessStepAlternativeType = create_fhir_type(
    "ExampleScenarioProcessStepAlternativeType",
    "fhir.resources.R4B.examplescenario.ExampleScenarioProcessStepAlternative",
)

ExampleScenarioProcessStepOperationType = create_fhir_type(
    "ExampleScenarioProcessStepOperationType",
    "fhir.resources.R4B.examplescenario.ExampleScenarioProcessStepOperation",
)

ExplanationOfBenefitType = create_fhir_type(
    "ExplanationOfBenefitType",
    "fhir.resources.R4B.explanationofbenefit.ExplanationOfBenefit",
)

ExplanationOfBenefitAccidentType = create_fhir_type(
    "ExplanationOfBenefitAccidentType",
    "fhir.resources.R4B.explanationofbenefit.ExplanationOfBenefitAccident",
)

ExplanationOfBenefitAddItemType = create_fhir_type(
    "ExplanationOfBenefitAddItemType",
    "fhir.resources.R4B.explanationofbenefit.ExplanationOfBenefitAddItem",
)

ExplanationOfBenefitAddItemDetailType = create_fhir_type(
    "ExplanationOfBenefitAddItemDetailType",
    "fhir.resources.R4B.explanationofbenefit.ExplanationOfBenefitAddItemDetail",
)

ExplanationOfBenefitAddItemDetailSubDetailType = create_fhir_type(
    "ExplanationOfBenefitAddItemDetailSubDetailType",
    "fhir.resources.R4B.explanationofbenefit.ExplanationOfBenefitAddItemDetailSubDetail",
)

ExplanationOfBenefitBenefitBalanceType = create_fhir_type(
    "ExplanationOfBenefitBenefitBalanceType",
    "fhir.resources.R4B.explanationofbenefit.ExplanationOfBenefitBenefitBalance",
)

ExplanationOfBenefitBenefitBalanceFinancialType = create_fhir_type(
    "ExplanationOfBenefitBenefitBalanceFinancialType",
    "fhir.resources.R4B.explanationofbenefit.ExplanationOfBenefitBenefitBalanceFinancial",
)

ExplanationOfBenefitCareTeamType = create_fhir_type(
    "ExplanationOfBenefitCareTeamType",
    "fhir.resources.R4B.explanationofbenefit.ExplanationOfBenefitCareTeam",
)

ExplanationOfBenefitDiagnosisType = create_fhir_type(
    "ExplanationOfBenefitDiagnosisType",
    "fhir.resources.R4B.explanationofbenefit.ExplanationOfBenefitDiagnosis",
)

ExplanationOfBenefitInsuranceType = create_fhir_type(
    "ExplanationOfBenefitInsuranceType",
    "fhir.resources.R4B.explanationofbenefit.ExplanationOfBenefitInsurance",
)

ExplanationOfBenefitItemType = create_fhir_type(
    "ExplanationOfBenefitItemType",
    "fhir.resources.R4B.explanationofbenefit.ExplanationOfBenefitItem",
)

ExplanationOfBenefitItemAdjudicationType = create_fhir_type(
    "ExplanationOfBenefitItemAdjudicationType",
    "fhir.resources.R4B.explanationofbenefit.ExplanationOfBenefitItemAdjudication",
)

ExplanationOfBenefitItemDetailType = create_fhir_type(
    "ExplanationOfBenefitItemDetailType",
    "fhir.resources.R4B.explanationofbenefit.ExplanationOfBenefitItemDetail",
)

ExplanationOfBenefitItemDetailSubDetailType = create_fhir_type(
    "ExplanationOfBenefitItemDetailSubDetailType",
    "fhir.resources.R4B.explanationofbenefit.ExplanationOfBenefitItemDetailSubDetail",
)

ExplanationOfBenefitPayeeType = create_fhir_type(
    "ExplanationOfBenefitPayeeType",
    "fhir.resources.R4B.explanationofbenefit.ExplanationOfBenefitPayee",
)

ExplanationOfBenefitPaymentType = create_fhir_type(
    "ExplanationOfBenefitPaymentType",
    "fhir.resources.R4B.explanationofbenefit.ExplanationOfBenefitPayment",
)

ExplanationOfBenefitProcedureType = create_fhir_type(
    "ExplanationOfBenefitProcedureType",
    "fhir.resources.R4B.explanationofbenefit.ExplanationOfBenefitProcedure",
)

ExplanationOfBenefitProcessNoteType = create_fhir_type(
    "ExplanationOfBenefitProcessNoteType",
    "fhir.resources.R4B.explanationofbenefit.ExplanationOfBenefitProcessNote",
)

ExplanationOfBenefitRelatedType = create_fhir_type(
    "ExplanationOfBenefitRelatedType",
    "fhir.resources.R4B.explanationofbenefit.ExplanationOfBenefitRelated",
)

ExplanationOfBenefitSupportingInfoType = create_fhir_type(
    "ExplanationOfBenefitSupportingInfoType",
    "fhir.resources.R4B.explanationofbenefit.ExplanationOfBenefitSupportingInfo",
)

ExplanationOfBenefitTotalType = create_fhir_type(
    "ExplanationOfBenefitTotalType",
    "fhir.resources.R4B.explanationofbenefit.ExplanationOfBenefitTotal",
)

ExpressionType = create_fhir_type(
    "ExpressionType", "fhir.resources.R4B.expression.Expression"
)

ExtensionType = create_fhir_type(
    "ExtensionType", "fhir.resources.R4B.extension.Extension"
)

FamilyMemberHistoryType = create_fhir_type(
    "FamilyMemberHistoryType",
    "fhir.resources.R4B.familymemberhistory.FamilyMemberHistory",
)

FamilyMemberHistoryConditionType = create_fhir_type(
    "FamilyMemberHistoryConditionType",
    "fhir.resources.R4B.familymemberhistory.FamilyMemberHistoryCondition",
)

FlagType = create_fhir_type("FlagType", "fhir.resources.R4B.flag.Flag")

GoalType = create_fhir_type("GoalType", "fhir.resources.R4B.goal.Goal")

GoalTargetType = create_fhir_type(
    "GoalTargetType", "fhir.resources.R4B.goal.GoalTarget"
)

GraphDefinitionType = create_fhir_type(
    "GraphDefinitionType", "fhir.resources.R4B.graphdefinition.GraphDefinition"
)

GraphDefinitionLinkType = create_fhir_type(
    "GraphDefinitionLinkType", "fhir.resources.R4B.graphdefinition.GraphDefinitionLink"
)

GraphDefinitionLinkTargetType = create_fhir_type(
    "GraphDefinitionLinkTargetType",
    "fhir.resources.R4B.graphdefinition.GraphDefinitionLinkTarget",
)

GraphDefinitionLinkTargetCompartmentType = create_fhir_type(
    "GraphDefinitionLinkTargetCompartmentType",
    "fhir.resources.R4B.graphdefinition.GraphDefinitionLinkTargetCompartment",
)

GroupType = create_fhir_type("GroupType", "fhir.resources.R4B.group.Group")

GroupCharacteristicType = create_fhir_type(
    "GroupCharacteristicType", "fhir.resources.R4B.group.GroupCharacteristic"
)

GroupMemberType = create_fhir_type(
    "GroupMemberType", "fhir.resources.R4B.group.GroupMember"
)

GuidanceResponseType = create_fhir_type(
    "GuidanceResponseType", "fhir.resources.R4B.guidanceresponse.GuidanceResponse"
)

HealthcareServiceType = create_fhir_type(
    "HealthcareServiceType", "fhir.resources.R4B.healthcareservice.HealthcareService"
)

HealthcareServiceAvailableTimeType = create_fhir_type(
    "HealthcareServiceAvailableTimeType",
    "fhir.resources.R4B.healthcareservice.HealthcareServiceAvailableTime",
)

HealthcareServiceEligibilityType = create_fhir_type(
    "HealthcareServiceEligibilityType",
    "fhir.resources.R4B.healthcareservice.HealthcareServiceEligibility",
)

HealthcareServiceNotAvailableType = create_fhir_type(
    "HealthcareServiceNotAvailableType",
    "fhir.resources.R4B.healthcareservice.HealthcareServiceNotAvailable",
)

HumanNameType = create_fhir_type(
    "HumanNameType", "fhir.resources.R4B.humanname.HumanName"
)

IdentifierType = create_fhir_type(
    "IdentifierType", "fhir.resources.R4B.identifier.Identifier"
)

ImagingStudyType = create_fhir_type(
    "ImagingStudyType", "fhir.resources.R4B.imagingstudy.ImagingStudy"
)

ImagingStudySeriesType = create_fhir_type(
    "ImagingStudySeriesType", "fhir.resources.R4B.imagingstudy.ImagingStudySeries"
)

ImagingStudySeriesInstanceType = create_fhir_type(
    "ImagingStudySeriesInstanceType",
    "fhir.resources.R4B.imagingstudy.ImagingStudySeriesInstance",
)

ImagingStudySeriesPerformerType = create_fhir_type(
    "ImagingStudySeriesPerformerType",
    "fhir.resources.R4B.imagingstudy.ImagingStudySeriesPerformer",
)

ImmunizationType = create_fhir_type(
    "ImmunizationType", "fhir.resources.R4B.immunization.Immunization"
)

ImmunizationEducationType = create_fhir_type(
    "ImmunizationEducationType", "fhir.resources.R4B.immunization.ImmunizationEducation"
)

ImmunizationEvaluationType = create_fhir_type(
    "ImmunizationEvaluationType",
    "fhir.resources.R4B.immunizationevaluation.ImmunizationEvaluation",
)

ImmunizationPerformerType = create_fhir_type(
    "ImmunizationPerformerType", "fhir.resources.R4B.immunization.ImmunizationPerformer"
)

ImmunizationProtocolAppliedType = create_fhir_type(
    "ImmunizationProtocolAppliedType",
    "fhir.resources.R4B.immunization.ImmunizationProtocolApplied",
)

ImmunizationReactionType = create_fhir_type(
    "ImmunizationReactionType", "fhir.resources.R4B.immunization.ImmunizationReaction"
)

ImmunizationRecommendationType = create_fhir_type(
    "ImmunizationRecommendationType",
    "fhir.resources.R4B.immunizationrecommendation.ImmunizationRecommendation",
)

ImmunizationRecommendationRecommendationType = create_fhir_type(
    "ImmunizationRecommendationRecommendationType",
    "fhir.resources.R4B.immunizationrecommendation.ImmunizationRecommendationRecommendation",
)

ImmunizationRecommendationRecommendationDateCriterionType = create_fhir_type(
    "ImmunizationRecommendationRecommendationDateCriterionType",
    "fhir.resources.R4B.immunizationrecommendation.ImmunizationRecommendationRecommendationDateCriterion",
)

ImplementationGuideType = create_fhir_type(
    "ImplementationGuideType",
    "fhir.resources.R4B.implementationguide.ImplementationGuide",
)

ImplementationGuideDefinitionType = create_fhir_type(
    "ImplementationGuideDefinitionType",
    "fhir.resources.R4B.implementationguide.ImplementationGuideDefinition",
)

ImplementationGuideDefinitionGroupingType = create_fhir_type(
    "ImplementationGuideDefinitionGroupingType",
    "fhir.resources.R4B.implementationguide.ImplementationGuideDefinitionGrouping",
)

ImplementationGuideDefinitionPageType = create_fhir_type(
    "ImplementationGuideDefinitionPageType",
    "fhir.resources.R4B.implementationguide.ImplementationGuideDefinitionPage",
)

ImplementationGuideDefinitionParameterType = create_fhir_type(
    "ImplementationGuideDefinitionParameterType",
    "fhir.resources.R4B.implementationguide.ImplementationGuideDefinitionParameter",
)

ImplementationGuideDefinitionResourceType = create_fhir_type(
    "ImplementationGuideDefinitionResourceType",
    "fhir.resources.R4B.implementationguide.ImplementationGuideDefinitionResource",
)

ImplementationGuideDefinitionTemplateType = create_fhir_type(
    "ImplementationGuideDefinitionTemplateType",
    "fhir.resources.R4B.implementationguide.ImplementationGuideDefinitionTemplate",
)

ImplementationGuideDependsOnType = create_fhir_type(
    "ImplementationGuideDependsOnType",
    "fhir.resources.R4B.implementationguide.ImplementationGuideDependsOn",
)

ImplementationGuideGlobalType = create_fhir_type(
    "ImplementationGuideGlobalType",
    "fhir.resources.R4B.implementationguide.ImplementationGuideGlobal",
)

ImplementationGuideManifestType = create_fhir_type(
    "ImplementationGuideManifestType",
    "fhir.resources.R4B.implementationguide.ImplementationGuideManifest",
)

ImplementationGuideManifestPageType = create_fhir_type(
    "ImplementationGuideManifestPageType",
    "fhir.resources.R4B.implementationguide.ImplementationGuideManifestPage",
)

ImplementationGuideManifestResourceType = create_fhir_type(
    "ImplementationGuideManifestResourceType",
    "fhir.resources.R4B.implementationguide.ImplementationGuideManifestResource",
)

IngredientType = create_fhir_type(
    "IngredientType", "fhir.resources.R4B.ingredient.Ingredient"
)

IngredientManufacturerType = create_fhir_type(
    "IngredientManufacturerType", "fhir.resources.R4B.ingredient.IngredientManufacturer"
)

IngredientSubstanceType = create_fhir_type(
    "IngredientSubstanceType", "fhir.resources.R4B.ingredient.IngredientSubstance"
)

IngredientSubstanceStrengthType = create_fhir_type(
    "IngredientSubstanceStrengthType",
    "fhir.resources.R4B.ingredient.IngredientSubstanceStrength",
)

IngredientSubstanceStrengthReferenceStrengthType = create_fhir_type(
    "IngredientSubstanceStrengthReferenceStrengthType",
    "fhir.resources.R4B.ingredient.IngredientSubstanceStrengthReferenceStrength",
)

InsurancePlanType = create_fhir_type(
    "InsurancePlanType", "fhir.resources.R4B.insuranceplan.InsurancePlan"
)

InsurancePlanContactType = create_fhir_type(
    "InsurancePlanContactType", "fhir.resources.R4B.insuranceplan.InsurancePlanContact"
)

InsurancePlanCoverageType = create_fhir_type(
    "InsurancePlanCoverageType",
    "fhir.resources.R4B.insuranceplan.InsurancePlanCoverage",
)

InsurancePlanCoverageBenefitType = create_fhir_type(
    "InsurancePlanCoverageBenefitType",
    "fhir.resources.R4B.insuranceplan.InsurancePlanCoverageBenefit",
)

InsurancePlanCoverageBenefitLimitType = create_fhir_type(
    "InsurancePlanCoverageBenefitLimitType",
    "fhir.resources.R4B.insuranceplan.InsurancePlanCoverageBenefitLimit",
)

InsurancePlanPlanType = create_fhir_type(
    "InsurancePlanPlanType", "fhir.resources.R4B.insuranceplan.InsurancePlanPlan"
)

InsurancePlanPlanGeneralCostType = create_fhir_type(
    "InsurancePlanPlanGeneralCostType",
    "fhir.resources.R4B.insuranceplan.InsurancePlanPlanGeneralCost",
)

InsurancePlanPlanSpecificCostType = create_fhir_type(
    "InsurancePlanPlanSpecificCostType",
    "fhir.resources.R4B.insuranceplan.InsurancePlanPlanSpecificCost",
)

InsurancePlanPlanSpecificCostBenefitType = create_fhir_type(
    "InsurancePlanPlanSpecificCostBenefitType",
    "fhir.resources.R4B.insuranceplan.InsurancePlanPlanSpecificCostBenefit",
)

InsurancePlanPlanSpecificCostBenefitCostType = create_fhir_type(
    "InsurancePlanPlanSpecificCostBenefitCostType",
    "fhir.resources.R4B.insuranceplan.InsurancePlanPlanSpecificCostBenefitCost",
)

InvoiceType = create_fhir_type("InvoiceType", "fhir.resources.R4B.invoice.Invoice")

InvoiceLineItemType = create_fhir_type(
    "InvoiceLineItemType", "fhir.resources.R4B.invoice.InvoiceLineItem"
)

InvoiceLineItemPriceComponentType = create_fhir_type(
    "InvoiceLineItemPriceComponentType",
    "fhir.resources.R4B.invoice.InvoiceLineItemPriceComponent",
)

InvoiceParticipantType = create_fhir_type(
    "InvoiceParticipantType", "fhir.resources.R4B.invoice.InvoiceParticipant"
)

LibraryType = create_fhir_type("LibraryType", "fhir.resources.R4B.library.Library")

LinkageType = create_fhir_type("LinkageType", "fhir.resources.R4B.linkage.Linkage")

LinkageItemType = create_fhir_type(
    "LinkageItemType", "fhir.resources.R4B.linkage.LinkageItem"
)

ListType = create_fhir_type("ListType", "fhir.resources.R4B.list.List")

ListEntryType = create_fhir_type("ListEntryType", "fhir.resources.R4B.list.ListEntry")

LocationType = create_fhir_type("LocationType", "fhir.resources.R4B.location.Location")

LocationHoursOfOperationType = create_fhir_type(
    "LocationHoursOfOperationType",
    "fhir.resources.R4B.location.LocationHoursOfOperation",
)

LocationPositionType = create_fhir_type(
    "LocationPositionType", "fhir.resources.R4B.location.LocationPosition"
)

ManufacturedItemDefinitionType = create_fhir_type(
    "ManufacturedItemDefinitionType",
    "fhir.resources.R4B.manufactureditemdefinition.ManufacturedItemDefinition",
)

ManufacturedItemDefinitionPropertyType = create_fhir_type(
    "ManufacturedItemDefinitionPropertyType",
    "fhir.resources.R4B.manufactureditemdefinition.ManufacturedItemDefinitionProperty",
)

MarketingStatusType = create_fhir_type(
    "MarketingStatusType", "fhir.resources.R4B.marketingstatus.MarketingStatus"
)

MeasureType = create_fhir_type("MeasureType", "fhir.resources.R4B.measure.Measure")

MeasureGroupType = create_fhir_type(
    "MeasureGroupType", "fhir.resources.R4B.measure.MeasureGroup"
)

MeasureGroupPopulationType = create_fhir_type(
    "MeasureGroupPopulationType", "fhir.resources.R4B.measure.MeasureGroupPopulation"
)

MeasureGroupStratifierType = create_fhir_type(
    "MeasureGroupStratifierType", "fhir.resources.R4B.measure.MeasureGroupStratifier"
)

MeasureGroupStratifierComponentType = create_fhir_type(
    "MeasureGroupStratifierComponentType",
    "fhir.resources.R4B.measure.MeasureGroupStratifierComponent",
)

MeasureReportType = create_fhir_type(
    "MeasureReportType", "fhir.resources.R4B.measurereport.MeasureReport"
)

MeasureReportGroupType = create_fhir_type(
    "MeasureReportGroupType", "fhir.resources.R4B.measurereport.MeasureReportGroup"
)

MeasureReportGroupPopulationType = create_fhir_type(
    "MeasureReportGroupPopulationType",
    "fhir.resources.R4B.measurereport.MeasureReportGroupPopulation",
)

MeasureReportGroupStratifierType = create_fhir_type(
    "MeasureReportGroupStratifierType",
    "fhir.resources.R4B.measurereport.MeasureReportGroupStratifier",
)

MeasureReportGroupStratifierStratumType = create_fhir_type(
    "MeasureReportGroupStratifierStratumType",
    "fhir.resources.R4B.measurereport.MeasureReportGroupStratifierStratum",
)

MeasureReportGroupStratifierStratumComponentType = create_fhir_type(
    "MeasureReportGroupStratifierStratumComponentType",
    "fhir.resources.R4B.measurereport.MeasureReportGroupStratifierStratumComponent",
)

MeasureReportGroupStratifierStratumPopulationType = create_fhir_type(
    "MeasureReportGroupStratifierStratumPopulationType",
    "fhir.resources.R4B.measurereport.MeasureReportGroupStratifierStratumPopulation",
)

MeasureSupplementalDataType = create_fhir_type(
    "MeasureSupplementalDataType", "fhir.resources.R4B.measure.MeasureSupplementalData"
)

MediaType = create_fhir_type("MediaType", "fhir.resources.R4B.media.Media")

MedicationType = create_fhir_type(
    "MedicationType", "fhir.resources.R4B.medication.Medication"
)

MedicationAdministrationType = create_fhir_type(
    "MedicationAdministrationType",
    "fhir.resources.R4B.medicationadministration.MedicationAdministration",
)

MedicationAdministrationDosageType = create_fhir_type(
    "MedicationAdministrationDosageType",
    "fhir.resources.R4B.medicationadministration.MedicationAdministrationDosage",
)

MedicationAdministrationPerformerType = create_fhir_type(
    "MedicationAdministrationPerformerType",
    "fhir.resources.R4B.medicationadministration.MedicationAdministrationPerformer",
)

MedicationBatchType = create_fhir_type(
    "MedicationBatchType", "fhir.resources.R4B.medication.MedicationBatch"
)

MedicationDispenseType = create_fhir_type(
    "MedicationDispenseType", "fhir.resources.R4B.medicationdispense.MedicationDispense"
)

MedicationDispensePerformerType = create_fhir_type(
    "MedicationDispensePerformerType",
    "fhir.resources.R4B.medicationdispense.MedicationDispensePerformer",
)

MedicationDispenseSubstitutionType = create_fhir_type(
    "MedicationDispenseSubstitutionType",
    "fhir.resources.R4B.medicationdispense.MedicationDispenseSubstitution",
)

MedicationIngredientType = create_fhir_type(
    "MedicationIngredientType", "fhir.resources.R4B.medication.MedicationIngredient"
)

MedicationKnowledgeType = create_fhir_type(
    "MedicationKnowledgeType",
    "fhir.resources.R4B.medicationknowledge.MedicationKnowledge",
)

MedicationKnowledgeAdministrationGuidelinesType = create_fhir_type(
    "MedicationKnowledgeAdministrationGuidelinesType",
    "fhir.resources.R4B.medicationknowledge.MedicationKnowledgeAdministrationGuidelines",
)

MedicationKnowledgeAdministrationGuidelinesDosageType = create_fhir_type(
    "MedicationKnowledgeAdministrationGuidelinesDosageType",
    "fhir.resources.R4B.medicationknowledge.MedicationKnowledgeAdministrationGuidelinesDosage",
)

MedicationKnowledgeAdministrationGuidelinesPatientCharacteristicsType = create_fhir_type(
    "MedicationKnowledgeAdministrationGuidelinesPatientCharacteristicsType",
    "fhir.resources.R4B.medicationknowledge.MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics",
)

MedicationKnowledgeCostType = create_fhir_type(
    "MedicationKnowledgeCostType",
    "fhir.resources.R4B.medicationknowledge.MedicationKnowledgeCost",
)

MedicationKnowledgeDrugCharacteristicType = create_fhir_type(
    "MedicationKnowledgeDrugCharacteristicType",
    "fhir.resources.R4B.medicationknowledge.MedicationKnowledgeDrugCharacteristic",
)

MedicationKnowledgeIngredientType = create_fhir_type(
    "MedicationKnowledgeIngredientType",
    "fhir.resources.R4B.medicationknowledge.MedicationKnowledgeIngredient",
)

MedicationKnowledgeKineticsType = create_fhir_type(
    "MedicationKnowledgeKineticsType",
    "fhir.resources.R4B.medicationknowledge.MedicationKnowledgeKinetics",
)

MedicationKnowledgeMedicineClassificationType = create_fhir_type(
    "MedicationKnowledgeMedicineClassificationType",
    "fhir.resources.R4B.medicationknowledge.MedicationKnowledgeMedicineClassification",
)

MedicationKnowledgeMonitoringProgramType = create_fhir_type(
    "MedicationKnowledgeMonitoringProgramType",
    "fhir.resources.R4B.medicationknowledge.MedicationKnowledgeMonitoringProgram",
)

MedicationKnowledgeMonographType = create_fhir_type(
    "MedicationKnowledgeMonographType",
    "fhir.resources.R4B.medicationknowledge.MedicationKnowledgeMonograph",
)

MedicationKnowledgePackagingType = create_fhir_type(
    "MedicationKnowledgePackagingType",
    "fhir.resources.R4B.medicationknowledge.MedicationKnowledgePackaging",
)

MedicationKnowledgeRegulatoryType = create_fhir_type(
    "MedicationKnowledgeRegulatoryType",
    "fhir.resources.R4B.medicationknowledge.MedicationKnowledgeRegulatory",
)

MedicationKnowledgeRegulatoryMaxDispenseType = create_fhir_type(
    "MedicationKnowledgeRegulatoryMaxDispenseType",
    "fhir.resources.R4B.medicationknowledge.MedicationKnowledgeRegulatoryMaxDispense",
)

MedicationKnowledgeRegulatoryScheduleType = create_fhir_type(
    "MedicationKnowledgeRegulatoryScheduleType",
    "fhir.resources.R4B.medicationknowledge.MedicationKnowledgeRegulatorySchedule",
)

MedicationKnowledgeRegulatorySubstitutionType = create_fhir_type(
    "MedicationKnowledgeRegulatorySubstitutionType",
    "fhir.resources.R4B.medicationknowledge.MedicationKnowledgeRegulatorySubstitution",
)

MedicationKnowledgeRelatedMedicationKnowledgeType = create_fhir_type(
    "MedicationKnowledgeRelatedMedicationKnowledgeType",
    "fhir.resources.R4B.medicationknowledge.MedicationKnowledgeRelatedMedicationKnowledge",
)

MedicationRequestType = create_fhir_type(
    "MedicationRequestType", "fhir.resources.R4B.medicationrequest.MedicationRequest"
)

MedicationRequestDispenseRequestType = create_fhir_type(
    "MedicationRequestDispenseRequestType",
    "fhir.resources.R4B.medicationrequest.MedicationRequestDispenseRequest",
)

MedicationRequestDispenseRequestInitialFillType = create_fhir_type(
    "MedicationRequestDispenseRequestInitialFillType",
    "fhir.resources.R4B.medicationrequest.MedicationRequestDispenseRequestInitialFill",
)

MedicationRequestSubstitutionType = create_fhir_type(
    "MedicationRequestSubstitutionType",
    "fhir.resources.R4B.medicationrequest.MedicationRequestSubstitution",
)

MedicationStatementType = create_fhir_type(
    "MedicationStatementType",
    "fhir.resources.R4B.medicationstatement.MedicationStatement",
)

MedicinalProductDefinitionType = create_fhir_type(
    "MedicinalProductDefinitionType",
    "fhir.resources.R4B.medicinalproductdefinition.MedicinalProductDefinition",
)

MedicinalProductDefinitionCharacteristicType = create_fhir_type(
    "MedicinalProductDefinitionCharacteristicType",
    "fhir.resources.R4B.medicinalproductdefinition.MedicinalProductDefinitionCharacteristic",
)

MedicinalProductDefinitionContactType = create_fhir_type(
    "MedicinalProductDefinitionContactType",
    "fhir.resources.R4B.medicinalproductdefinition.MedicinalProductDefinitionContact",
)

MedicinalProductDefinitionCrossReferenceType = create_fhir_type(
    "MedicinalProductDefinitionCrossReferenceType",
    "fhir.resources.R4B.medicinalproductdefinition.MedicinalProductDefinitionCrossReference",
)

MedicinalProductDefinitionNameType = create_fhir_type(
    "MedicinalProductDefinitionNameType",
    "fhir.resources.R4B.medicinalproductdefinition.MedicinalProductDefinitionName",
)

MedicinalProductDefinitionNameCountryLanguageType = create_fhir_type(
    "MedicinalProductDefinitionNameCountryLanguageType",
    "fhir.resources.R4B.medicinalproductdefinition.MedicinalProductDefinitionNameCountryLanguage",
)

MedicinalProductDefinitionNameNamePartType = create_fhir_type(
    "MedicinalProductDefinitionNameNamePartType",
    "fhir.resources.R4B.medicinalproductdefinition.MedicinalProductDefinitionNameNamePart",
)

MedicinalProductDefinitionOperationType = create_fhir_type(
    "MedicinalProductDefinitionOperationType",
    "fhir.resources.R4B.medicinalproductdefinition.MedicinalProductDefinitionOperation",
)

MessageDefinitionType = create_fhir_type(
    "MessageDefinitionType", "fhir.resources.R4B.messagedefinition.MessageDefinition"
)

MessageDefinitionAllowedResponseType = create_fhir_type(
    "MessageDefinitionAllowedResponseType",
    "fhir.resources.R4B.messagedefinition.MessageDefinitionAllowedResponse",
)

MessageDefinitionFocusType = create_fhir_type(
    "MessageDefinitionFocusType",
    "fhir.resources.R4B.messagedefinition.MessageDefinitionFocus",
)

MessageHeaderType = create_fhir_type(
    "MessageHeaderType", "fhir.resources.R4B.messageheader.MessageHeader"
)

MessageHeaderDestinationType = create_fhir_type(
    "MessageHeaderDestinationType",
    "fhir.resources.R4B.messageheader.MessageHeaderDestination",
)

MessageHeaderResponseType = create_fhir_type(
    "MessageHeaderResponseType",
    "fhir.resources.R4B.messageheader.MessageHeaderResponse",
)

MessageHeaderSourceType = create_fhir_type(
    "MessageHeaderSourceType", "fhir.resources.R4B.messageheader.MessageHeaderSource"
)

MetaType = create_fhir_type("MetaType", "fhir.resources.R4B.meta.Meta")

MolecularSequenceType = create_fhir_type(
    "MolecularSequenceType", "fhir.resources.R4B.molecularsequence.MolecularSequence"
)

MolecularSequenceQualityType = create_fhir_type(
    "MolecularSequenceQualityType",
    "fhir.resources.R4B.molecularsequence.MolecularSequenceQuality",
)

MolecularSequenceQualityRocType = create_fhir_type(
    "MolecularSequenceQualityRocType",
    "fhir.resources.R4B.molecularsequence.MolecularSequenceQualityRoc",
)

MolecularSequenceReferenceSeqType = create_fhir_type(
    "MolecularSequenceReferenceSeqType",
    "fhir.resources.R4B.molecularsequence.MolecularSequenceReferenceSeq",
)

MolecularSequenceRepositoryType = create_fhir_type(
    "MolecularSequenceRepositoryType",
    "fhir.resources.R4B.molecularsequence.MolecularSequenceRepository",
)

MolecularSequenceStructureVariantType = create_fhir_type(
    "MolecularSequenceStructureVariantType",
    "fhir.resources.R4B.molecularsequence.MolecularSequenceStructureVariant",
)

MolecularSequenceStructureVariantInnerType = create_fhir_type(
    "MolecularSequenceStructureVariantInnerType",
    "fhir.resources.R4B.molecularsequence.MolecularSequenceStructureVariantInner",
)

MolecularSequenceStructureVariantOuterType = create_fhir_type(
    "MolecularSequenceStructureVariantOuterType",
    "fhir.resources.R4B.molecularsequence.MolecularSequenceStructureVariantOuter",
)

MolecularSequenceVariantType = create_fhir_type(
    "MolecularSequenceVariantType",
    "fhir.resources.R4B.molecularsequence.MolecularSequenceVariant",
)

MoneyType = create_fhir_type("MoneyType", "fhir.resources.R4B.money.Money")

NamingSystemType = create_fhir_type(
    "NamingSystemType", "fhir.resources.R4B.namingsystem.NamingSystem"
)

NamingSystemUniqueIdType = create_fhir_type(
    "NamingSystemUniqueIdType", "fhir.resources.R4B.namingsystem.NamingSystemUniqueId"
)

NarrativeType = create_fhir_type(
    "NarrativeType", "fhir.resources.R4B.narrative.Narrative"
)

NutritionOrderType = create_fhir_type(
    "NutritionOrderType", "fhir.resources.R4B.nutritionorder.NutritionOrder"
)

NutritionOrderEnteralFormulaType = create_fhir_type(
    "NutritionOrderEnteralFormulaType",
    "fhir.resources.R4B.nutritionorder.NutritionOrderEnteralFormula",
)

NutritionOrderEnteralFormulaAdministrationType = create_fhir_type(
    "NutritionOrderEnteralFormulaAdministrationType",
    "fhir.resources.R4B.nutritionorder.NutritionOrderEnteralFormulaAdministration",
)

NutritionOrderOralDietType = create_fhir_type(
    "NutritionOrderOralDietType",
    "fhir.resources.R4B.nutritionorder.NutritionOrderOralDiet",
)

NutritionOrderOralDietNutrientType = create_fhir_type(
    "NutritionOrderOralDietNutrientType",
    "fhir.resources.R4B.nutritionorder.NutritionOrderOralDietNutrient",
)

NutritionOrderOralDietTextureType = create_fhir_type(
    "NutritionOrderOralDietTextureType",
    "fhir.resources.R4B.nutritionorder.NutritionOrderOralDietTexture",
)

NutritionOrderSupplementType = create_fhir_type(
    "NutritionOrderSupplementType",
    "fhir.resources.R4B.nutritionorder.NutritionOrderSupplement",
)

NutritionProductType = create_fhir_type(
    "NutritionProductType", "fhir.resources.R4B.nutritionproduct.NutritionProduct"
)

NutritionProductIngredientType = create_fhir_type(
    "NutritionProductIngredientType",
    "fhir.resources.R4B.nutritionproduct.NutritionProductIngredient",
)

NutritionProductInstanceType = create_fhir_type(
    "NutritionProductInstanceType",
    "fhir.resources.R4B.nutritionproduct.NutritionProductInstance",
)

NutritionProductNutrientType = create_fhir_type(
    "NutritionProductNutrientType",
    "fhir.resources.R4B.nutritionproduct.NutritionProductNutrient",
)

NutritionProductProductCharacteristicType = create_fhir_type(
    "NutritionProductProductCharacteristicType",
    "fhir.resources.R4B.nutritionproduct.NutritionProductProductCharacteristic",
)

ObservationType = create_fhir_type(
    "ObservationType", "fhir.resources.R4B.observation.Observation"
)

ObservationComponentType = create_fhir_type(
    "ObservationComponentType", "fhir.resources.R4B.observation.ObservationComponent"
)

ObservationDefinitionType = create_fhir_type(
    "ObservationDefinitionType",
    "fhir.resources.R4B.observationdefinition.ObservationDefinition",
)

ObservationDefinitionQualifiedIntervalType = create_fhir_type(
    "ObservationDefinitionQualifiedIntervalType",
    "fhir.resources.R4B.observationdefinition.ObservationDefinitionQualifiedInterval",
)

ObservationDefinitionQuantitativeDetailsType = create_fhir_type(
    "ObservationDefinitionQuantitativeDetailsType",
    "fhir.resources.R4B.observationdefinition.ObservationDefinitionQuantitativeDetails",
)

ObservationReferenceRangeType = create_fhir_type(
    "ObservationReferenceRangeType",
    "fhir.resources.R4B.observation.ObservationReferenceRange",
)

OperationDefinitionType = create_fhir_type(
    "OperationDefinitionType",
    "fhir.resources.R4B.operationdefinition.OperationDefinition",
)

OperationDefinitionOverloadType = create_fhir_type(
    "OperationDefinitionOverloadType",
    "fhir.resources.R4B.operationdefinition.OperationDefinitionOverload",
)

OperationDefinitionParameterType = create_fhir_type(
    "OperationDefinitionParameterType",
    "fhir.resources.R4B.operationdefinition.OperationDefinitionParameter",
)

OperationDefinitionParameterBindingType = create_fhir_type(
    "OperationDefinitionParameterBindingType",
    "fhir.resources.R4B.operationdefinition.OperationDefinitionParameterBinding",
)

OperationDefinitionParameterReferencedFromType = create_fhir_type(
    "OperationDefinitionParameterReferencedFromType",
    "fhir.resources.R4B.operationdefinition.OperationDefinitionParameterReferencedFrom",
)

OperationOutcomeType = create_fhir_type(
    "OperationOutcomeType", "fhir.resources.R4B.operationoutcome.OperationOutcome"
)

OperationOutcomeIssueType = create_fhir_type(
    "OperationOutcomeIssueType",
    "fhir.resources.R4B.operationoutcome.OperationOutcomeIssue",
)

OrganizationType = create_fhir_type(
    "OrganizationType", "fhir.resources.R4B.organization.Organization"
)

OrganizationAffiliationType = create_fhir_type(
    "OrganizationAffiliationType",
    "fhir.resources.R4B.organizationaffiliation.OrganizationAffiliation",
)

OrganizationContactType = create_fhir_type(
    "OrganizationContactType", "fhir.resources.R4B.organization.OrganizationContact"
)

PackagedProductDefinitionType = create_fhir_type(
    "PackagedProductDefinitionType",
    "fhir.resources.R4B.packagedproductdefinition.PackagedProductDefinition",
)

PackagedProductDefinitionLegalStatusOfSupplyType = create_fhir_type(
    "PackagedProductDefinitionLegalStatusOfSupplyType",
    "fhir.resources.R4B.packagedproductdefinition.PackagedProductDefinitionLegalStatusOfSupply",
)

PackagedProductDefinitionPackageType = create_fhir_type(
    "PackagedProductDefinitionPackageType",
    "fhir.resources.R4B.packagedproductdefinition.PackagedProductDefinitionPackage",
)

PackagedProductDefinitionPackageContainedItemType = create_fhir_type(
    "PackagedProductDefinitionPackageContainedItemType",
    "fhir.resources.R4B.packagedproductdefinition.PackagedProductDefinitionPackageContainedItem",
)

PackagedProductDefinitionPackagePropertyType = create_fhir_type(
    "PackagedProductDefinitionPackagePropertyType",
    "fhir.resources.R4B.packagedproductdefinition.PackagedProductDefinitionPackageProperty",
)

PackagedProductDefinitionPackageShelfLifeStorageType = create_fhir_type(
    "PackagedProductDefinitionPackageShelfLifeStorageType",
    "fhir.resources.R4B.packagedproductdefinition.PackagedProductDefinitionPackageShelfLifeStorage",
)

ParameterDefinitionType = create_fhir_type(
    "ParameterDefinitionType",
    "fhir.resources.R4B.parameterdefinition.ParameterDefinition",
)

ParametersType = create_fhir_type(
    "ParametersType", "fhir.resources.R4B.parameters.Parameters"
)

ParametersParameterType = create_fhir_type(
    "ParametersParameterType", "fhir.resources.R4B.parameters.ParametersParameter"
)

PatientType = create_fhir_type("PatientType", "fhir.resources.R4B.patient.Patient")

PatientCommunicationType = create_fhir_type(
    "PatientCommunicationType", "fhir.resources.R4B.patient.PatientCommunication"
)

PatientContactType = create_fhir_type(
    "PatientContactType", "fhir.resources.R4B.patient.PatientContact"
)

PatientLinkType = create_fhir_type(
    "PatientLinkType", "fhir.resources.R4B.patient.PatientLink"
)

PaymentNoticeType = create_fhir_type(
    "PaymentNoticeType", "fhir.resources.R4B.paymentnotice.PaymentNotice"
)

PaymentReconciliationType = create_fhir_type(
    "PaymentReconciliationType",
    "fhir.resources.R4B.paymentreconciliation.PaymentReconciliation",
)

PaymentReconciliationDetailType = create_fhir_type(
    "PaymentReconciliationDetailType",
    "fhir.resources.R4B.paymentreconciliation.PaymentReconciliationDetail",
)

PaymentReconciliationProcessNoteType = create_fhir_type(
    "PaymentReconciliationProcessNoteType",
    "fhir.resources.R4B.paymentreconciliation.PaymentReconciliationProcessNote",
)

PeriodType = create_fhir_type("PeriodType", "fhir.resources.R4B.period.Period")

PersonType = create_fhir_type("PersonType", "fhir.resources.R4B.person.Person")

PersonLinkType = create_fhir_type(
    "PersonLinkType", "fhir.resources.R4B.person.PersonLink"
)

PlanDefinitionType = create_fhir_type(
    "PlanDefinitionType", "fhir.resources.R4B.plandefinition.PlanDefinition"
)

PlanDefinitionActionType = create_fhir_type(
    "PlanDefinitionActionType", "fhir.resources.R4B.plandefinition.PlanDefinitionAction"
)

PlanDefinitionActionConditionType = create_fhir_type(
    "PlanDefinitionActionConditionType",
    "fhir.resources.R4B.plandefinition.PlanDefinitionActionCondition",
)

PlanDefinitionActionDynamicValueType = create_fhir_type(
    "PlanDefinitionActionDynamicValueType",
    "fhir.resources.R4B.plandefinition.PlanDefinitionActionDynamicValue",
)

PlanDefinitionActionParticipantType = create_fhir_type(
    "PlanDefinitionActionParticipantType",
    "fhir.resources.R4B.plandefinition.PlanDefinitionActionParticipant",
)

PlanDefinitionActionRelatedActionType = create_fhir_type(
    "PlanDefinitionActionRelatedActionType",
    "fhir.resources.R4B.plandefinition.PlanDefinitionActionRelatedAction",
)

PlanDefinitionGoalType = create_fhir_type(
    "PlanDefinitionGoalType", "fhir.resources.R4B.plandefinition.PlanDefinitionGoal"
)

PlanDefinitionGoalTargetType = create_fhir_type(
    "PlanDefinitionGoalTargetType",
    "fhir.resources.R4B.plandefinition.PlanDefinitionGoalTarget",
)

PopulationType = create_fhir_type(
    "PopulationType", "fhir.resources.R4B.population.Population"
)

PractitionerType = create_fhir_type(
    "PractitionerType", "fhir.resources.R4B.practitioner.Practitioner"
)

PractitionerQualificationType = create_fhir_type(
    "PractitionerQualificationType",
    "fhir.resources.R4B.practitioner.PractitionerQualification",
)

PractitionerRoleType = create_fhir_type(
    "PractitionerRoleType", "fhir.resources.R4B.practitionerrole.PractitionerRole"
)

PractitionerRoleAvailableTimeType = create_fhir_type(
    "PractitionerRoleAvailableTimeType",
    "fhir.resources.R4B.practitionerrole.PractitionerRoleAvailableTime",
)

PractitionerRoleNotAvailableType = create_fhir_type(
    "PractitionerRoleNotAvailableType",
    "fhir.resources.R4B.practitionerrole.PractitionerRoleNotAvailable",
)

ProcedureType = create_fhir_type(
    "ProcedureType", "fhir.resources.R4B.procedure.Procedure"
)

ProcedureFocalDeviceType = create_fhir_type(
    "ProcedureFocalDeviceType", "fhir.resources.R4B.procedure.ProcedureFocalDevice"
)

ProcedurePerformerType = create_fhir_type(
    "ProcedurePerformerType", "fhir.resources.R4B.procedure.ProcedurePerformer"
)

ProdCharacteristicType = create_fhir_type(
    "ProdCharacteristicType", "fhir.resources.R4B.prodcharacteristic.ProdCharacteristic"
)

ProductShelfLifeType = create_fhir_type(
    "ProductShelfLifeType", "fhir.resources.R4B.productshelflife.ProductShelfLife"
)

ProvenanceType = create_fhir_type(
    "ProvenanceType", "fhir.resources.R4B.provenance.Provenance"
)

ProvenanceAgentType = create_fhir_type(
    "ProvenanceAgentType", "fhir.resources.R4B.provenance.ProvenanceAgent"
)

ProvenanceEntityType = create_fhir_type(
    "ProvenanceEntityType", "fhir.resources.R4B.provenance.ProvenanceEntity"
)

QuantityType = create_fhir_type("QuantityType", "fhir.resources.R4B.quantity.Quantity")

QuestionnaireType = create_fhir_type(
    "QuestionnaireType", "fhir.resources.R4B.questionnaire.Questionnaire"
)

QuestionnaireItemType = create_fhir_type(
    "QuestionnaireItemType", "fhir.resources.R4B.questionnaire.QuestionnaireItem"
)

QuestionnaireItemAnswerOptionType = create_fhir_type(
    "QuestionnaireItemAnswerOptionType",
    "fhir.resources.R4B.questionnaire.QuestionnaireItemAnswerOption",
)

QuestionnaireItemEnableWhenType = create_fhir_type(
    "QuestionnaireItemEnableWhenType",
    "fhir.resources.R4B.questionnaire.QuestionnaireItemEnableWhen",
)

QuestionnaireItemInitialType = create_fhir_type(
    "QuestionnaireItemInitialType",
    "fhir.resources.R4B.questionnaire.QuestionnaireItemInitial",
)

QuestionnaireResponseType = create_fhir_type(
    "QuestionnaireResponseType",
    "fhir.resources.R4B.questionnaireresponse.QuestionnaireResponse",
)

QuestionnaireResponseItemType = create_fhir_type(
    "QuestionnaireResponseItemType",
    "fhir.resources.R4B.questionnaireresponse.QuestionnaireResponseItem",
)

QuestionnaireResponseItemAnswerType = create_fhir_type(
    "QuestionnaireResponseItemAnswerType",
    "fhir.resources.R4B.questionnaireresponse.QuestionnaireResponseItemAnswer",
)

RangeType = create_fhir_type("RangeType", "fhir.resources.R4B.range.Range")

RatioType = create_fhir_type("RatioType", "fhir.resources.R4B.ratio.Ratio")

RatioRangeType = create_fhir_type(
    "RatioRangeType", "fhir.resources.R4B.ratiorange.RatioRange"
)

ReferenceType = create_fhir_type(
    "ReferenceType", "fhir.resources.R4B.reference.Reference"
)

RegulatedAuthorizationType = create_fhir_type(
    "RegulatedAuthorizationType",
    "fhir.resources.R4B.regulatedauthorization.RegulatedAuthorization",
)

RegulatedAuthorizationCaseType = create_fhir_type(
    "RegulatedAuthorizationCaseType",
    "fhir.resources.R4B.regulatedauthorization.RegulatedAuthorizationCase",
)

RelatedArtifactType = create_fhir_type(
    "RelatedArtifactType", "fhir.resources.R4B.relatedartifact.RelatedArtifact"
)

RelatedPersonType = create_fhir_type(
    "RelatedPersonType", "fhir.resources.R4B.relatedperson.RelatedPerson"
)

RelatedPersonCommunicationType = create_fhir_type(
    "RelatedPersonCommunicationType",
    "fhir.resources.R4B.relatedperson.RelatedPersonCommunication",
)

RequestGroupType = create_fhir_type(
    "RequestGroupType", "fhir.resources.R4B.requestgroup.RequestGroup"
)

RequestGroupActionType = create_fhir_type(
    "RequestGroupActionType", "fhir.resources.R4B.requestgroup.RequestGroupAction"
)

RequestGroupActionConditionType = create_fhir_type(
    "RequestGroupActionConditionType",
    "fhir.resources.R4B.requestgroup.RequestGroupActionCondition",
)

RequestGroupActionRelatedActionType = create_fhir_type(
    "RequestGroupActionRelatedActionType",
    "fhir.resources.R4B.requestgroup.RequestGroupActionRelatedAction",
)

ResearchDefinitionType = create_fhir_type(
    "ResearchDefinitionType", "fhir.resources.R4B.researchdefinition.ResearchDefinition"
)

ResearchElementDefinitionType = create_fhir_type(
    "ResearchElementDefinitionType",
    "fhir.resources.R4B.researchelementdefinition.ResearchElementDefinition",
)

ResearchElementDefinitionCharacteristicType = create_fhir_type(
    "ResearchElementDefinitionCharacteristicType",
    "fhir.resources.R4B.researchelementdefinition.ResearchElementDefinitionCharacteristic",
)

ResearchStudyType = create_fhir_type(
    "ResearchStudyType", "fhir.resources.R4B.researchstudy.ResearchStudy"
)

ResearchStudyArmType = create_fhir_type(
    "ResearchStudyArmType", "fhir.resources.R4B.researchstudy.ResearchStudyArm"
)

ResearchStudyObjectiveType = create_fhir_type(
    "ResearchStudyObjectiveType",
    "fhir.resources.R4B.researchstudy.ResearchStudyObjective",
)

ResearchSubjectType = create_fhir_type(
    "ResearchSubjectType", "fhir.resources.R4B.researchsubject.ResearchSubject"
)

RiskAssessmentType = create_fhir_type(
    "RiskAssessmentType", "fhir.resources.R4B.riskassessment.RiskAssessment"
)

RiskAssessmentPredictionType = create_fhir_type(
    "RiskAssessmentPredictionType",
    "fhir.resources.R4B.riskassessment.RiskAssessmentPrediction",
)

SampledDataType = create_fhir_type(
    "SampledDataType", "fhir.resources.R4B.sampleddata.SampledData"
)

ScheduleType = create_fhir_type("ScheduleType", "fhir.resources.R4B.schedule.Schedule")

SearchParameterType = create_fhir_type(
    "SearchParameterType", "fhir.resources.R4B.searchparameter.SearchParameter"
)

SearchParameterComponentType = create_fhir_type(
    "SearchParameterComponentType",
    "fhir.resources.R4B.searchparameter.SearchParameterComponent",
)

ServiceRequestType = create_fhir_type(
    "ServiceRequestType", "fhir.resources.R4B.servicerequest.ServiceRequest"
)

SignatureType = create_fhir_type(
    "SignatureType", "fhir.resources.R4B.signature.Signature"
)

SlotType = create_fhir_type("SlotType", "fhir.resources.R4B.slot.Slot")

SpecimenType = create_fhir_type("SpecimenType", "fhir.resources.R4B.specimen.Specimen")

SpecimenCollectionType = create_fhir_type(
    "SpecimenCollectionType", "fhir.resources.R4B.specimen.SpecimenCollection"
)

SpecimenContainerType = create_fhir_type(
    "SpecimenContainerType", "fhir.resources.R4B.specimen.SpecimenContainer"
)

SpecimenDefinitionType = create_fhir_type(
    "SpecimenDefinitionType", "fhir.resources.R4B.specimendefinition.SpecimenDefinition"
)

SpecimenDefinitionTypeTestedType = create_fhir_type(
    "SpecimenDefinitionTypeTestedType",
    "fhir.resources.R4B.specimendefinition.SpecimenDefinitionTypeTested",
)

SpecimenDefinitionTypeTestedContainerType = create_fhir_type(
    "SpecimenDefinitionTypeTestedContainerType",
    "fhir.resources.R4B.specimendefinition.SpecimenDefinitionTypeTestedContainer",
)

SpecimenDefinitionTypeTestedContainerAdditiveType = create_fhir_type(
    "SpecimenDefinitionTypeTestedContainerAdditiveType",
    "fhir.resources.R4B.specimendefinition.SpecimenDefinitionTypeTestedContainerAdditive",
)

SpecimenDefinitionTypeTestedHandlingType = create_fhir_type(
    "SpecimenDefinitionTypeTestedHandlingType",
    "fhir.resources.R4B.specimendefinition.SpecimenDefinitionTypeTestedHandling",
)

SpecimenProcessingType = create_fhir_type(
    "SpecimenProcessingType", "fhir.resources.R4B.specimen.SpecimenProcessing"
)

StructureDefinitionType = create_fhir_type(
    "StructureDefinitionType",
    "fhir.resources.R4B.structuredefinition.StructureDefinition",
)

StructureDefinitionContextType = create_fhir_type(
    "StructureDefinitionContextType",
    "fhir.resources.R4B.structuredefinition.StructureDefinitionContext",
)

StructureDefinitionDifferentialType = create_fhir_type(
    "StructureDefinitionDifferentialType",
    "fhir.resources.R4B.structuredefinition.StructureDefinitionDifferential",
)

StructureDefinitionMappingType = create_fhir_type(
    "StructureDefinitionMappingType",
    "fhir.resources.R4B.structuredefinition.StructureDefinitionMapping",
)

StructureDefinitionSnapshotType = create_fhir_type(
    "StructureDefinitionSnapshotType",
    "fhir.resources.R4B.structuredefinition.StructureDefinitionSnapshot",
)

StructureMapType = create_fhir_type(
    "StructureMapType", "fhir.resources.R4B.structuremap.StructureMap"
)

StructureMapGroupType = create_fhir_type(
    "StructureMapGroupType", "fhir.resources.R4B.structuremap.StructureMapGroup"
)

StructureMapGroupInputType = create_fhir_type(
    "StructureMapGroupInputType",
    "fhir.resources.R4B.structuremap.StructureMapGroupInput",
)

StructureMapGroupRuleType = create_fhir_type(
    "StructureMapGroupRuleType", "fhir.resources.R4B.structuremap.StructureMapGroupRule"
)

StructureMapGroupRuleDependentType = create_fhir_type(
    "StructureMapGroupRuleDependentType",
    "fhir.resources.R4B.structuremap.StructureMapGroupRuleDependent",
)

StructureMapGroupRuleSourceType = create_fhir_type(
    "StructureMapGroupRuleSourceType",
    "fhir.resources.R4B.structuremap.StructureMapGroupRuleSource",
)

StructureMapGroupRuleTargetType = create_fhir_type(
    "StructureMapGroupRuleTargetType",
    "fhir.resources.R4B.structuremap.StructureMapGroupRuleTarget",
)

StructureMapGroupRuleTargetParameterType = create_fhir_type(
    "StructureMapGroupRuleTargetParameterType",
    "fhir.resources.R4B.structuremap.StructureMapGroupRuleTargetParameter",
)

StructureMapStructureType = create_fhir_type(
    "StructureMapStructureType", "fhir.resources.R4B.structuremap.StructureMapStructure"
)

SubscriptionType = create_fhir_type(
    "SubscriptionType", "fhir.resources.R4B.subscription.Subscription"
)

SubscriptionChannelType = create_fhir_type(
    "SubscriptionChannelType", "fhir.resources.R4B.subscription.SubscriptionChannel"
)

SubscriptionStatusType = create_fhir_type(
    "SubscriptionStatusType", "fhir.resources.R4B.subscriptionstatus.SubscriptionStatus"
)

SubscriptionStatusNotificationEventType = create_fhir_type(
    "SubscriptionStatusNotificationEventType",
    "fhir.resources.R4B.subscriptionstatus.SubscriptionStatusNotificationEvent",
)

SubscriptionTopicType = create_fhir_type(
    "SubscriptionTopicType", "fhir.resources.R4B.subscriptiontopic.SubscriptionTopic"
)

SubscriptionTopicCanFilterByType = create_fhir_type(
    "SubscriptionTopicCanFilterByType",
    "fhir.resources.R4B.subscriptiontopic.SubscriptionTopicCanFilterBy",
)

SubscriptionTopicEventTriggerType = create_fhir_type(
    "SubscriptionTopicEventTriggerType",
    "fhir.resources.R4B.subscriptiontopic.SubscriptionTopicEventTrigger",
)

SubscriptionTopicNotificationShapeType = create_fhir_type(
    "SubscriptionTopicNotificationShapeType",
    "fhir.resources.R4B.subscriptiontopic.SubscriptionTopicNotificationShape",
)

SubscriptionTopicResourceTriggerType = create_fhir_type(
    "SubscriptionTopicResourceTriggerType",
    "fhir.resources.R4B.subscriptiontopic.SubscriptionTopicResourceTrigger",
)

SubscriptionTopicResourceTriggerQueryCriteriaType = create_fhir_type(
    "SubscriptionTopicResourceTriggerQueryCriteriaType",
    "fhir.resources.R4B.subscriptiontopic.SubscriptionTopicResourceTriggerQueryCriteria",
)

SubstanceType = create_fhir_type(
    "SubstanceType", "fhir.resources.R4B.substance.Substance"
)

SubstanceDefinitionType = create_fhir_type(
    "SubstanceDefinitionType",
    "fhir.resources.R4B.substancedefinition.SubstanceDefinition",
)

SubstanceDefinitionCodeType = create_fhir_type(
    "SubstanceDefinitionCodeType",
    "fhir.resources.R4B.substancedefinition.SubstanceDefinitionCode",
)

SubstanceDefinitionMoietyType = create_fhir_type(
    "SubstanceDefinitionMoietyType",
    "fhir.resources.R4B.substancedefinition.SubstanceDefinitionMoiety",
)

SubstanceDefinitionMolecularWeightType = create_fhir_type(
    "SubstanceDefinitionMolecularWeightType",
    "fhir.resources.R4B.substancedefinition.SubstanceDefinitionMolecularWeight",
)

SubstanceDefinitionNameType = create_fhir_type(
    "SubstanceDefinitionNameType",
    "fhir.resources.R4B.substancedefinition.SubstanceDefinitionName",
)

SubstanceDefinitionNameOfficialType = create_fhir_type(
    "SubstanceDefinitionNameOfficialType",
    "fhir.resources.R4B.substancedefinition.SubstanceDefinitionNameOfficial",
)

SubstanceDefinitionPropertyType = create_fhir_type(
    "SubstanceDefinitionPropertyType",
    "fhir.resources.R4B.substancedefinition.SubstanceDefinitionProperty",
)

SubstanceDefinitionRelationshipType = create_fhir_type(
    "SubstanceDefinitionRelationshipType",
    "fhir.resources.R4B.substancedefinition.SubstanceDefinitionRelationship",
)

SubstanceDefinitionSourceMaterialType = create_fhir_type(
    "SubstanceDefinitionSourceMaterialType",
    "fhir.resources.R4B.substancedefinition.SubstanceDefinitionSourceMaterial",
)

SubstanceDefinitionStructureType = create_fhir_type(
    "SubstanceDefinitionStructureType",
    "fhir.resources.R4B.substancedefinition.SubstanceDefinitionStructure",
)

SubstanceDefinitionStructureRepresentationType = create_fhir_type(
    "SubstanceDefinitionStructureRepresentationType",
    "fhir.resources.R4B.substancedefinition.SubstanceDefinitionStructureRepresentation",
)

SubstanceIngredientType = create_fhir_type(
    "SubstanceIngredientType", "fhir.resources.R4B.substance.SubstanceIngredient"
)

SubstanceInstanceType = create_fhir_type(
    "SubstanceInstanceType", "fhir.resources.R4B.substance.SubstanceInstance"
)

SupplyDeliveryType = create_fhir_type(
    "SupplyDeliveryType", "fhir.resources.R4B.supplydelivery.SupplyDelivery"
)

SupplyDeliverySuppliedItemType = create_fhir_type(
    "SupplyDeliverySuppliedItemType",
    "fhir.resources.R4B.supplydelivery.SupplyDeliverySuppliedItem",
)

SupplyRequestType = create_fhir_type(
    "SupplyRequestType", "fhir.resources.R4B.supplyrequest.SupplyRequest"
)

SupplyRequestParameterType = create_fhir_type(
    "SupplyRequestParameterType",
    "fhir.resources.R4B.supplyrequest.SupplyRequestParameter",
)

TaskType = create_fhir_type("TaskType", "fhir.resources.R4B.task.Task")

TaskInputType = create_fhir_type("TaskInputType", "fhir.resources.R4B.task.TaskInput")

TaskOutputType = create_fhir_type(
    "TaskOutputType", "fhir.resources.R4B.task.TaskOutput"
)

TaskRestrictionType = create_fhir_type(
    "TaskRestrictionType", "fhir.resources.R4B.task.TaskRestriction"
)

TerminologyCapabilitiesType = create_fhir_type(
    "TerminologyCapabilitiesType",
    "fhir.resources.R4B.terminologycapabilities.TerminologyCapabilities",
)

TerminologyCapabilitiesClosureType = create_fhir_type(
    "TerminologyCapabilitiesClosureType",
    "fhir.resources.R4B.terminologycapabilities.TerminologyCapabilitiesClosure",
)

TerminologyCapabilitiesCodeSystemType = create_fhir_type(
    "TerminologyCapabilitiesCodeSystemType",
    "fhir.resources.R4B.terminologycapabilities.TerminologyCapabilitiesCodeSystem",
)

TerminologyCapabilitiesCodeSystemVersionType = create_fhir_type(
    "TerminologyCapabilitiesCodeSystemVersionType",
    "fhir.resources.R4B.terminologycapabilities.TerminologyCapabilitiesCodeSystemVersion",
)

TerminologyCapabilitiesCodeSystemVersionFilterType = create_fhir_type(
    "TerminologyCapabilitiesCodeSystemVersionFilterType",
    "fhir.resources.R4B.terminologycapabilities.TerminologyCapabilitiesCodeSystemVersionFilter",
)

TerminologyCapabilitiesExpansionType = create_fhir_type(
    "TerminologyCapabilitiesExpansionType",
    "fhir.resources.R4B.terminologycapabilities.TerminologyCapabilitiesExpansion",
)

TerminologyCapabilitiesExpansionParameterType = create_fhir_type(
    "TerminologyCapabilitiesExpansionParameterType",
    "fhir.resources.R4B.terminologycapabilities.TerminologyCapabilitiesExpansionParameter",
)

TerminologyCapabilitiesImplementationType = create_fhir_type(
    "TerminologyCapabilitiesImplementationType",
    "fhir.resources.R4B.terminologycapabilities.TerminologyCapabilitiesImplementation",
)

TerminologyCapabilitiesSoftwareType = create_fhir_type(
    "TerminologyCapabilitiesSoftwareType",
    "fhir.resources.R4B.terminologycapabilities.TerminologyCapabilitiesSoftware",
)

TerminologyCapabilitiesTranslationType = create_fhir_type(
    "TerminologyCapabilitiesTranslationType",
    "fhir.resources.R4B.terminologycapabilities.TerminologyCapabilitiesTranslation",
)

TerminologyCapabilitiesValidateCodeType = create_fhir_type(
    "TerminologyCapabilitiesValidateCodeType",
    "fhir.resources.R4B.terminologycapabilities.TerminologyCapabilitiesValidateCode",
)

TestReportType = create_fhir_type(
    "TestReportType", "fhir.resources.R4B.testreport.TestReport"
)

TestReportParticipantType = create_fhir_type(
    "TestReportParticipantType", "fhir.resources.R4B.testreport.TestReportParticipant"
)

TestReportSetupType = create_fhir_type(
    "TestReportSetupType", "fhir.resources.R4B.testreport.TestReportSetup"
)

TestReportSetupActionType = create_fhir_type(
    "TestReportSetupActionType", "fhir.resources.R4B.testreport.TestReportSetupAction"
)

TestReportSetupActionAssertType = create_fhir_type(
    "TestReportSetupActionAssertType",
    "fhir.resources.R4B.testreport.TestReportSetupActionAssert",
)

TestReportSetupActionOperationType = create_fhir_type(
    "TestReportSetupActionOperationType",
    "fhir.resources.R4B.testreport.TestReportSetupActionOperation",
)

TestReportTeardownType = create_fhir_type(
    "TestReportTeardownType", "fhir.resources.R4B.testreport.TestReportTeardown"
)

TestReportTeardownActionType = create_fhir_type(
    "TestReportTeardownActionType",
    "fhir.resources.R4B.testreport.TestReportTeardownAction",
)

TestReportTestType = create_fhir_type(
    "TestReportTestType", "fhir.resources.R4B.testreport.TestReportTest"
)

TestReportTestActionType = create_fhir_type(
    "TestReportTestActionType", "fhir.resources.R4B.testreport.TestReportTestAction"
)

TestScriptType = create_fhir_type(
    "TestScriptType", "fhir.resources.R4B.testscript.TestScript"
)

TestScriptDestinationType = create_fhir_type(
    "TestScriptDestinationType", "fhir.resources.R4B.testscript.TestScriptDestination"
)

TestScriptFixtureType = create_fhir_type(
    "TestScriptFixtureType", "fhir.resources.R4B.testscript.TestScriptFixture"
)

TestScriptMetadataType = create_fhir_type(
    "TestScriptMetadataType", "fhir.resources.R4B.testscript.TestScriptMetadata"
)

TestScriptMetadataCapabilityType = create_fhir_type(
    "TestScriptMetadataCapabilityType",
    "fhir.resources.R4B.testscript.TestScriptMetadataCapability",
)

TestScriptMetadataLinkType = create_fhir_type(
    "TestScriptMetadataLinkType", "fhir.resources.R4B.testscript.TestScriptMetadataLink"
)

TestScriptOriginType = create_fhir_type(
    "TestScriptOriginType", "fhir.resources.R4B.testscript.TestScriptOrigin"
)

TestScriptSetupType = create_fhir_type(
    "TestScriptSetupType", "fhir.resources.R4B.testscript.TestScriptSetup"
)

TestScriptSetupActionType = create_fhir_type(
    "TestScriptSetupActionType", "fhir.resources.R4B.testscript.TestScriptSetupAction"
)

TestScriptSetupActionAssertType = create_fhir_type(
    "TestScriptSetupActionAssertType",
    "fhir.resources.R4B.testscript.TestScriptSetupActionAssert",
)

TestScriptSetupActionOperationType = create_fhir_type(
    "TestScriptSetupActionOperationType",
    "fhir.resources.R4B.testscript.TestScriptSetupActionOperation",
)

TestScriptSetupActionOperationRequestHeaderType = create_fhir_type(
    "TestScriptSetupActionOperationRequestHeaderType",
    "fhir.resources.R4B.testscript.TestScriptSetupActionOperationRequestHeader",
)

TestScriptTeardownType = create_fhir_type(
    "TestScriptTeardownType", "fhir.resources.R4B.testscript.TestScriptTeardown"
)

TestScriptTeardownActionType = create_fhir_type(
    "TestScriptTeardownActionType",
    "fhir.resources.R4B.testscript.TestScriptTeardownAction",
)

TestScriptTestType = create_fhir_type(
    "TestScriptTestType", "fhir.resources.R4B.testscript.TestScriptTest"
)

TestScriptTestActionType = create_fhir_type(
    "TestScriptTestActionType", "fhir.resources.R4B.testscript.TestScriptTestAction"
)

TestScriptVariableType = create_fhir_type(
    "TestScriptVariableType", "fhir.resources.R4B.testscript.TestScriptVariable"
)

TimingType = create_fhir_type("TimingType", "fhir.resources.R4B.timing.Timing")

TimingRepeatType = create_fhir_type(
    "TimingRepeatType", "fhir.resources.R4B.timing.TimingRepeat"
)

TriggerDefinitionType = create_fhir_type(
    "TriggerDefinitionType", "fhir.resources.R4B.triggerdefinition.TriggerDefinition"
)

UsageContextType = create_fhir_type(
    "UsageContextType", "fhir.resources.R4B.usagecontext.UsageContext"
)

ValueSetType = create_fhir_type("ValueSetType", "fhir.resources.R4B.valueset.ValueSet")

ValueSetComposeType = create_fhir_type(
    "ValueSetComposeType", "fhir.resources.R4B.valueset.ValueSetCompose"
)

ValueSetComposeIncludeType = create_fhir_type(
    "ValueSetComposeIncludeType", "fhir.resources.R4B.valueset.ValueSetComposeInclude"
)

ValueSetComposeIncludeConceptType = create_fhir_type(
    "ValueSetComposeIncludeConceptType",
    "fhir.resources.R4B.valueset.ValueSetComposeIncludeConcept",
)

ValueSetComposeIncludeConceptDesignationType = create_fhir_type(
    "ValueSetComposeIncludeConceptDesignationType",
    "fhir.resources.R4B.valueset.ValueSetComposeIncludeConceptDesignation",
)

ValueSetComposeIncludeFilterType = create_fhir_type(
    "ValueSetComposeIncludeFilterType",
    "fhir.resources.R4B.valueset.ValueSetComposeIncludeFilter",
)

ValueSetExpansionType = create_fhir_type(
    "ValueSetExpansionType", "fhir.resources.R4B.valueset.ValueSetExpansion"
)

ValueSetExpansionContainsType = create_fhir_type(
    "ValueSetExpansionContainsType",
    "fhir.resources.R4B.valueset.ValueSetExpansionContains",
)

ValueSetExpansionParameterType = create_fhir_type(
    "ValueSetExpansionParameterType",
    "fhir.resources.R4B.valueset.ValueSetExpansionParameter",
)

VerificationResultType = create_fhir_type(
    "VerificationResultType", "fhir.resources.R4B.verificationresult.VerificationResult"
)

VerificationResultAttestationType = create_fhir_type(
    "VerificationResultAttestationType",
    "fhir.resources.R4B.verificationresult.VerificationResultAttestation",
)

VerificationResultPrimarySourceType = create_fhir_type(
    "VerificationResultPrimarySourceType",
    "fhir.resources.R4B.verificationresult.VerificationResultPrimarySource",
)

VerificationResultValidatorType = create_fhir_type(
    "VerificationResultValidatorType",
    "fhir.resources.R4B.verificationresult.VerificationResultValidator",
)

VisionPrescriptionType = create_fhir_type(
    "VisionPrescriptionType", "fhir.resources.R4B.visionprescription.VisionPrescription"
)

VisionPrescriptionLensSpecificationType = create_fhir_type(
    "VisionPrescriptionLensSpecificationType",
    "fhir.resources.R4B.visionprescription.VisionPrescriptionLensSpecification",
)

VisionPrescriptionLensSpecificationPrismType = create_fhir_type(
    "VisionPrescriptionLensSpecificationPrismType",
    "fhir.resources.R4B.visionprescription.VisionPrescriptionLensSpecificationPrism",
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
    "AdministrableProductDefinitionType",
    "AdministrableProductDefinitionPropertyType",
    "AdministrableProductDefinitionRouteOfAdministrationType",
    "AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesType",
    "AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriodType",
    "AdverseEventType",
    "AdverseEventSuspectEntityType",
    "AdverseEventSuspectEntityCausalityType",
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
    "BiologicallyDerivedProductType",
    "BiologicallyDerivedProductCollectionType",
    "BiologicallyDerivedProductManipulationType",
    "BiologicallyDerivedProductProcessingType",
    "BiologicallyDerivedProductStorageType",
    "BodyStructureType",
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
    "CarePlanActivityDetailType",
    "CareTeamType",
    "CareTeamParticipantType",
    "CatalogEntryType",
    "CatalogEntryRelatedEntryType",
    "ChargeItemType",
    "ChargeItemDefinitionType",
    "ChargeItemDefinitionApplicabilityType",
    "ChargeItemDefinitionPropertyGroupType",
    "ChargeItemDefinitionPropertyGroupPriceComponentType",
    "ChargeItemPerformerType",
    "CitationType",
    "CitationCitedArtifactType",
    "CitationCitedArtifactAbstractType",
    "CitationCitedArtifactClassificationType",
    "CitationCitedArtifactClassificationWhoClassifiedType",
    "CitationCitedArtifactContributorshipType",
    "CitationCitedArtifactContributorshipEntryType",
    "CitationCitedArtifactContributorshipEntryAffiliationInfoType",
    "CitationCitedArtifactContributorshipEntryContributionInstanceType",
    "CitationCitedArtifactContributorshipSummaryType",
    "CitationCitedArtifactPartType",
    "CitationCitedArtifactPublicationFormType",
    "CitationCitedArtifactPublicationFormPeriodicReleaseType",
    "CitationCitedArtifactPublicationFormPeriodicReleaseDateOfPublicationType",
    "CitationCitedArtifactPublicationFormPublishedInType",
    "CitationCitedArtifactRelatesToType",
    "CitationCitedArtifactStatusDateType",
    "CitationCitedArtifactTitleType",
    "CitationCitedArtifactVersionType",
    "CitationCitedArtifactWebLocationType",
    "CitationClassificationType",
    "CitationRelatesToType",
    "CitationStatusDateType",
    "CitationSummaryType",
    "ClaimType",
    "ClaimAccidentType",
    "ClaimCareTeamType",
    "ClaimDiagnosisType",
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
    "ClaimResponseAddItemDetailSubDetailType",
    "ClaimResponseErrorType",
    "ClaimResponseInsuranceType",
    "ClaimResponseItemType",
    "ClaimResponseItemAdjudicationType",
    "ClaimResponseItemDetailType",
    "ClaimResponseItemDetailSubDetailType",
    "ClaimResponsePaymentType",
    "ClaimResponseProcessNoteType",
    "ClaimResponseTotalType",
    "ClaimSupportingInfoType",
    "ClinicalImpressionType",
    "ClinicalImpressionFindingType",
    "ClinicalImpressionInvestigationType",
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
    "ConsentPolicyType",
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
    "CoverageEligibilityRequestInsuranceType",
    "CoverageEligibilityRequestItemType",
    "CoverageEligibilityRequestItemDiagnosisType",
    "CoverageEligibilityRequestSupportingInfoType",
    "CoverageEligibilityResponseType",
    "CoverageEligibilityResponseErrorType",
    "CoverageEligibilityResponseInsuranceType",
    "CoverageEligibilityResponseInsuranceItemType",
    "CoverageEligibilityResponseInsuranceItemBenefitType",
    "DataRequirementType",
    "DataRequirementCodeFilterType",
    "DataRequirementDateFilterType",
    "DataRequirementSortType",
    "DetectedIssueType",
    "DetectedIssueEvidenceType",
    "DetectedIssueMitigationType",
    "DeviceType",
    "DeviceDefinitionType",
    "DeviceDefinitionCapabilityType",
    "DeviceDefinitionDeviceNameType",
    "DeviceDefinitionMaterialType",
    "DeviceDefinitionPropertyType",
    "DeviceDefinitionSpecializationType",
    "DeviceDefinitionUdiDeviceIdentifierType",
    "DeviceDeviceNameType",
    "DeviceMetricType",
    "DeviceMetricCalibrationType",
    "DevicePropertyType",
    "DeviceRequestType",
    "DeviceRequestParameterType",
    "DeviceSpecializationType",
    "DeviceUdiCarrierType",
    "DeviceUseStatementType",
    "DeviceVersionType",
    "DiagnosticReportType",
    "DiagnosticReportMediaType",
    "DistanceType",
    "DocumentManifestType",
    "DocumentManifestRelatedType",
    "DocumentReferenceType",
    "DocumentReferenceContentType",
    "DocumentReferenceContextType",
    "DocumentReferenceRelatesToType",
    "DomainResourceType",
    "DosageType",
    "DosageDoseAndRateType",
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
    "EventDefinitionType",
    "EvidenceType",
    "EvidenceCertaintyType",
    "EvidenceReportType",
    "EvidenceReportRelatesToType",
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
    "EvidenceVariableCharacteristicTimeFromStartType",
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
    "ExplanationOfBenefitAddItemDetailType",
    "ExplanationOfBenefitAddItemDetailSubDetailType",
    "ExplanationOfBenefitBenefitBalanceType",
    "ExplanationOfBenefitBenefitBalanceFinancialType",
    "ExplanationOfBenefitCareTeamType",
    "ExplanationOfBenefitDiagnosisType",
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
    "ExplanationOfBenefitSupportingInfoType",
    "ExplanationOfBenefitTotalType",
    "ExpressionType",
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
    "HealthcareServiceEligibilityType",
    "HealthcareServiceNotAvailableType",
    "HumanNameType",
    "IdentifierType",
    "ImagingStudyType",
    "ImagingStudySeriesType",
    "ImagingStudySeriesInstanceType",
    "ImagingStudySeriesPerformerType",
    "ImmunizationType",
    "ImmunizationEducationType",
    "ImmunizationEvaluationType",
    "ImmunizationPerformerType",
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
    "InsurancePlanContactType",
    "InsurancePlanCoverageType",
    "InsurancePlanCoverageBenefitType",
    "InsurancePlanCoverageBenefitLimitType",
    "InsurancePlanPlanType",
    "InsurancePlanPlanGeneralCostType",
    "InsurancePlanPlanSpecificCostType",
    "InsurancePlanPlanSpecificCostBenefitType",
    "InsurancePlanPlanSpecificCostBenefitCostType",
    "InvoiceType",
    "InvoiceLineItemType",
    "InvoiceLineItemPriceComponentType",
    "InvoiceParticipantType",
    "LibraryType",
    "LinkageType",
    "LinkageItemType",
    "ListType",
    "ListEntryType",
    "LocationType",
    "LocationHoursOfOperationType",
    "LocationPositionType",
    "ManufacturedItemDefinitionType",
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
    "MediaType",
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
    "MedicationKnowledgeAdministrationGuidelinesType",
    "MedicationKnowledgeAdministrationGuidelinesDosageType",
    "MedicationKnowledgeAdministrationGuidelinesPatientCharacteristicsType",
    "MedicationKnowledgeCostType",
    "MedicationKnowledgeDrugCharacteristicType",
    "MedicationKnowledgeIngredientType",
    "MedicationKnowledgeKineticsType",
    "MedicationKnowledgeMedicineClassificationType",
    "MedicationKnowledgeMonitoringProgramType",
    "MedicationKnowledgeMonographType",
    "MedicationKnowledgePackagingType",
    "MedicationKnowledgeRegulatoryType",
    "MedicationKnowledgeRegulatoryMaxDispenseType",
    "MedicationKnowledgeRegulatoryScheduleType",
    "MedicationKnowledgeRegulatorySubstitutionType",
    "MedicationKnowledgeRelatedMedicationKnowledgeType",
    "MedicationRequestType",
    "MedicationRequestDispenseRequestType",
    "MedicationRequestDispenseRequestInitialFillType",
    "MedicationRequestSubstitutionType",
    "MedicationStatementType",
    "MedicinalProductDefinitionType",
    "MedicinalProductDefinitionCharacteristicType",
    "MedicinalProductDefinitionContactType",
    "MedicinalProductDefinitionCrossReferenceType",
    "MedicinalProductDefinitionNameType",
    "MedicinalProductDefinitionNameCountryLanguageType",
    "MedicinalProductDefinitionNameNamePartType",
    "MedicinalProductDefinitionOperationType",
    "MessageDefinitionType",
    "MessageDefinitionAllowedResponseType",
    "MessageDefinitionFocusType",
    "MessageHeaderType",
    "MessageHeaderDestinationType",
    "MessageHeaderResponseType",
    "MessageHeaderSourceType",
    "MetaType",
    "MolecularSequenceType",
    "MolecularSequenceQualityType",
    "MolecularSequenceQualityRocType",
    "MolecularSequenceReferenceSeqType",
    "MolecularSequenceRepositoryType",
    "MolecularSequenceStructureVariantType",
    "MolecularSequenceStructureVariantInnerType",
    "MolecularSequenceStructureVariantOuterType",
    "MolecularSequenceVariantType",
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
    "NutritionProductType",
    "NutritionProductIngredientType",
    "NutritionProductInstanceType",
    "NutritionProductNutrientType",
    "NutritionProductProductCharacteristicType",
    "ObservationType",
    "ObservationComponentType",
    "ObservationDefinitionType",
    "ObservationDefinitionQualifiedIntervalType",
    "ObservationDefinitionQuantitativeDetailsType",
    "ObservationReferenceRangeType",
    "OperationDefinitionType",
    "OperationDefinitionOverloadType",
    "OperationDefinitionParameterType",
    "OperationDefinitionParameterBindingType",
    "OperationDefinitionParameterReferencedFromType",
    "OperationOutcomeType",
    "OperationOutcomeIssueType",
    "OrganizationType",
    "OrganizationAffiliationType",
    "OrganizationContactType",
    "PackagedProductDefinitionType",
    "PackagedProductDefinitionLegalStatusOfSupplyType",
    "PackagedProductDefinitionPackageType",
    "PackagedProductDefinitionPackageContainedItemType",
    "PackagedProductDefinitionPackagePropertyType",
    "PackagedProductDefinitionPackageShelfLifeStorageType",
    "ParameterDefinitionType",
    "ParametersType",
    "ParametersParameterType",
    "PatientType",
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
    "PopulationType",
    "PractitionerType",
    "PractitionerQualificationType",
    "PractitionerRoleType",
    "PractitionerRoleAvailableTimeType",
    "PractitionerRoleNotAvailableType",
    "ProcedureType",
    "ProcedureFocalDeviceType",
    "ProcedurePerformerType",
    "ProdCharacteristicType",
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
    "RequestGroupType",
    "RequestGroupActionType",
    "RequestGroupActionConditionType",
    "RequestGroupActionRelatedActionType",
    "ResearchDefinitionType",
    "ResearchElementDefinitionType",
    "ResearchElementDefinitionCharacteristicType",
    "ResearchStudyType",
    "ResearchStudyArmType",
    "ResearchStudyObjectiveType",
    "ResearchSubjectType",
    "ResourceType",
    "RiskAssessmentType",
    "RiskAssessmentPredictionType",
    "SampledDataType",
    "ScheduleType",
    "SearchParameterType",
    "SearchParameterComponentType",
    "ServiceRequestType",
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
    "SpecimenProcessingType",
    "StructureDefinitionType",
    "StructureDefinitionContextType",
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
    "SubstanceInstanceType",
    "SupplyDeliveryType",
    "SupplyDeliverySuppliedItemType",
    "SupplyRequestType",
    "SupplyRequestParameterType",
    "TaskType",
    "TaskInputType",
    "TaskOutputType",
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
    "TestScriptSetupType",
    "TestScriptSetupActionType",
    "TestScriptSetupActionAssertType",
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
    "VerificationResultType",
    "VerificationResultAttestationType",
    "VerificationResultPrimarySourceType",
    "VerificationResultValidatorType",
    "VisionPrescriptionType",
    "VisionPrescriptionLensSpecificationType",
    "VisionPrescriptionLensSpecificationPrismType",
]
