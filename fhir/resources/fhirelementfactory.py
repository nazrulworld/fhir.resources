#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1 on 2020-04-10.
#  2020, SMART Health IT.


class FHIRElementFactory(object):
    """ Factory class to instantiate resources by resource name.
    """

    @classmethod
    def instantiate(cls, resource_type, jsondict, strict=True):
        """ Instantiate a resource of the type correlating to "resource_type".

        :param str resource_type: The name/type of the resource to instantiate
        :param dict jsondict: The JSON dictionary to use for data
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        :returns: A resource of the respective type or `Element`
        """
        if "Account" == resource_type:
            from . import account

            return account.Account(jsondict, strict)
        if "AccountCoverage" == resource_type:
            from . import account

            return account.AccountCoverage(jsondict, strict)
        if "AccountGuarantor" == resource_type:
            from . import account

            return account.AccountGuarantor(jsondict, strict)
        if "ActivityDefinition" == resource_type:
            from . import activitydefinition

            return activitydefinition.ActivityDefinition(jsondict, strict)
        if "ActivityDefinitionDynamicValue" == resource_type:
            from . import activitydefinition

            return activitydefinition.ActivityDefinitionDynamicValue(jsondict, strict)
        if "ActivityDefinitionParticipant" == resource_type:
            from . import activitydefinition

            return activitydefinition.ActivityDefinitionParticipant(jsondict, strict)
        if "Address" == resource_type:
            from . import address

            return address.Address(jsondict, strict)
        if "AdverseEvent" == resource_type:
            from . import adverseevent

            return adverseevent.AdverseEvent(jsondict, strict)
        if "AdverseEventSuspectEntity" == resource_type:
            from . import adverseevent

            return adverseevent.AdverseEventSuspectEntity(jsondict, strict)
        if "AdverseEventSuspectEntityCausality" == resource_type:
            from . import adverseevent

            return adverseevent.AdverseEventSuspectEntityCausality(jsondict, strict)
        if "Age" == resource_type:
            from . import age

            return age.Age(jsondict, strict)
        if "AllergyIntolerance" == resource_type:
            from . import allergyintolerance

            return allergyintolerance.AllergyIntolerance(jsondict, strict)
        if "AllergyIntoleranceReaction" == resource_type:
            from . import allergyintolerance

            return allergyintolerance.AllergyIntoleranceReaction(jsondict, strict)
        if "Annotation" == resource_type:
            from . import annotation

            return annotation.Annotation(jsondict, strict)
        if "Appointment" == resource_type:
            from . import appointment

            return appointment.Appointment(jsondict, strict)
        if "AppointmentParticipant" == resource_type:
            from . import appointment

            return appointment.AppointmentParticipant(jsondict, strict)
        if "AppointmentResponse" == resource_type:
            from . import appointmentresponse

            return appointmentresponse.AppointmentResponse(jsondict, strict)
        if "Attachment" == resource_type:
            from . import attachment

            return attachment.Attachment(jsondict, strict)
        if "AuditEvent" == resource_type:
            from . import auditevent

            return auditevent.AuditEvent(jsondict, strict)
        if "AuditEventAgent" == resource_type:
            from . import auditevent

            return auditevent.AuditEventAgent(jsondict, strict)
        if "AuditEventAgentNetwork" == resource_type:
            from . import auditevent

            return auditevent.AuditEventAgentNetwork(jsondict, strict)
        if "AuditEventEntity" == resource_type:
            from . import auditevent

            return auditevent.AuditEventEntity(jsondict, strict)
        if "AuditEventEntityDetail" == resource_type:
            from . import auditevent

            return auditevent.AuditEventEntityDetail(jsondict, strict)
        if "AuditEventSource" == resource_type:
            from . import auditevent

            return auditevent.AuditEventSource(jsondict, strict)
        if "BackboneElement" == resource_type:
            from . import backboneelement

            return backboneelement.BackboneElement(jsondict, strict)
        if "Basic" == resource_type:
            from . import basic

            return basic.Basic(jsondict, strict)
        if "Binary" == resource_type:
            from . import binary

            return binary.Binary(jsondict, strict)
        if "BiologicallyDerivedProduct" == resource_type:
            from . import biologicallyderivedproduct

            return biologicallyderivedproduct.BiologicallyDerivedProduct(
                jsondict, strict
            )
        if "BiologicallyDerivedProductCollection" == resource_type:
            from . import biologicallyderivedproduct

            return biologicallyderivedproduct.BiologicallyDerivedProductCollection(
                jsondict, strict
            )
        if "BiologicallyDerivedProductManipulation" == resource_type:
            from . import biologicallyderivedproduct

            return biologicallyderivedproduct.BiologicallyDerivedProductManipulation(
                jsondict, strict
            )
        if "BiologicallyDerivedProductProcessing" == resource_type:
            from . import biologicallyderivedproduct

            return biologicallyderivedproduct.BiologicallyDerivedProductProcessing(
                jsondict, strict
            )
        if "BiologicallyDerivedProductStorage" == resource_type:
            from . import biologicallyderivedproduct

            return biologicallyderivedproduct.BiologicallyDerivedProductStorage(
                jsondict, strict
            )
        if "BodyStructure" == resource_type:
            from . import bodystructure

            return bodystructure.BodyStructure(jsondict, strict)
        if "Bundle" == resource_type:
            from . import bundle

            return bundle.Bundle(jsondict, strict)
        if "BundleEntry" == resource_type:
            from . import bundle

            return bundle.BundleEntry(jsondict, strict)
        if "BundleEntryRequest" == resource_type:
            from . import bundle

            return bundle.BundleEntryRequest(jsondict, strict)
        if "BundleEntryResponse" == resource_type:
            from . import bundle

            return bundle.BundleEntryResponse(jsondict, strict)
        if "BundleEntrySearch" == resource_type:
            from . import bundle

            return bundle.BundleEntrySearch(jsondict, strict)
        if "BundleLink" == resource_type:
            from . import bundle

            return bundle.BundleLink(jsondict, strict)
        if "CapabilityStatement" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatement(jsondict, strict)
        if "CapabilityStatementDocument" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementDocument(jsondict, strict)
        if "CapabilityStatementImplementation" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementImplementation(
                jsondict, strict
            )
        if "CapabilityStatementMessaging" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementMessaging(jsondict, strict)
        if "CapabilityStatementMessagingEndpoint" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementMessagingEndpoint(
                jsondict, strict
            )
        if "CapabilityStatementMessagingSupportedMessage" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementMessagingSupportedMessage(
                jsondict, strict
            )
        if "CapabilityStatementRest" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementRest(jsondict, strict)
        if "CapabilityStatementRestInteraction" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementRestInteraction(
                jsondict, strict
            )
        if "CapabilityStatementRestResource" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementRestResource(jsondict, strict)
        if "CapabilityStatementRestResourceInteraction" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementRestResourceInteraction(
                jsondict, strict
            )
        if "CapabilityStatementRestResourceOperation" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementRestResourceOperation(
                jsondict, strict
            )
        if "CapabilityStatementRestResourceSearchParam" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementRestResourceSearchParam(
                jsondict, strict
            )
        if "CapabilityStatementRestSecurity" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementRestSecurity(jsondict, strict)
        if "CapabilityStatementSoftware" == resource_type:
            from . import capabilitystatement

            return capabilitystatement.CapabilityStatementSoftware(jsondict, strict)
        if "CarePlan" == resource_type:
            from . import careplan

            return careplan.CarePlan(jsondict, strict)
        if "CarePlanActivity" == resource_type:
            from . import careplan

            return careplan.CarePlanActivity(jsondict, strict)
        if "CarePlanActivityDetail" == resource_type:
            from . import careplan

            return careplan.CarePlanActivityDetail(jsondict, strict)
        if "CareTeam" == resource_type:
            from . import careteam

            return careteam.CareTeam(jsondict, strict)
        if "CareTeamParticipant" == resource_type:
            from . import careteam

            return careteam.CareTeamParticipant(jsondict, strict)
        if "CatalogEntry" == resource_type:
            from . import catalogentry

            return catalogentry.CatalogEntry(jsondict, strict)
        if "CatalogEntryRelatedEntry" == resource_type:
            from . import catalogentry

            return catalogentry.CatalogEntryRelatedEntry(jsondict, strict)
        if "ChargeItem" == resource_type:
            from . import chargeitem

            return chargeitem.ChargeItem(jsondict, strict)
        if "ChargeItemDefinition" == resource_type:
            from . import chargeitemdefinition

            return chargeitemdefinition.ChargeItemDefinition(jsondict, strict)
        if "ChargeItemDefinitionApplicability" == resource_type:
            from . import chargeitemdefinition

            return chargeitemdefinition.ChargeItemDefinitionApplicability(
                jsondict, strict
            )
        if "ChargeItemDefinitionPropertyGroup" == resource_type:
            from . import chargeitemdefinition

            return chargeitemdefinition.ChargeItemDefinitionPropertyGroup(
                jsondict, strict
            )
        if "ChargeItemDefinitionPropertyGroupPriceComponent" == resource_type:
            from . import chargeitemdefinition

            return chargeitemdefinition.ChargeItemDefinitionPropertyGroupPriceComponent(
                jsondict, strict
            )
        if "ChargeItemPerformer" == resource_type:
            from . import chargeitem

            return chargeitem.ChargeItemPerformer(jsondict, strict)
        if "Claim" == resource_type:
            from . import claim

            return claim.Claim(jsondict, strict)
        if "ClaimAccident" == resource_type:
            from . import claim

            return claim.ClaimAccident(jsondict, strict)
        if "ClaimCareTeam" == resource_type:
            from . import claim

            return claim.ClaimCareTeam(jsondict, strict)
        if "ClaimDiagnosis" == resource_type:
            from . import claim

            return claim.ClaimDiagnosis(jsondict, strict)
        if "ClaimInsurance" == resource_type:
            from . import claim

            return claim.ClaimInsurance(jsondict, strict)
        if "ClaimItem" == resource_type:
            from . import claim

            return claim.ClaimItem(jsondict, strict)
        if "ClaimItemDetail" == resource_type:
            from . import claim

            return claim.ClaimItemDetail(jsondict, strict)
        if "ClaimItemDetailSubDetail" == resource_type:
            from . import claim

            return claim.ClaimItemDetailSubDetail(jsondict, strict)
        if "ClaimPayee" == resource_type:
            from . import claim

            return claim.ClaimPayee(jsondict, strict)
        if "ClaimProcedure" == resource_type:
            from . import claim

            return claim.ClaimProcedure(jsondict, strict)
        if "ClaimRelated" == resource_type:
            from . import claim

            return claim.ClaimRelated(jsondict, strict)
        if "ClaimResponse" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponse(jsondict, strict)
        if "ClaimResponseAddItem" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponseAddItem(jsondict, strict)
        if "ClaimResponseAddItemDetail" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponseAddItemDetail(jsondict, strict)
        if "ClaimResponseAddItemDetailSubDetail" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponseAddItemDetailSubDetail(jsondict, strict)
        if "ClaimResponseError" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponseError(jsondict, strict)
        if "ClaimResponseInsurance" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponseInsurance(jsondict, strict)
        if "ClaimResponseItem" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponseItem(jsondict, strict)
        if "ClaimResponseItemAdjudication" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponseItemAdjudication(jsondict, strict)
        if "ClaimResponseItemDetail" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponseItemDetail(jsondict, strict)
        if "ClaimResponseItemDetailSubDetail" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponseItemDetailSubDetail(jsondict, strict)
        if "ClaimResponsePayment" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponsePayment(jsondict, strict)
        if "ClaimResponseProcessNote" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponseProcessNote(jsondict, strict)
        if "ClaimResponseTotal" == resource_type:
            from . import claimresponse

            return claimresponse.ClaimResponseTotal(jsondict, strict)
        if "ClaimSupportingInfo" == resource_type:
            from . import claim

            return claim.ClaimSupportingInfo(jsondict, strict)
        if "ClinicalImpression" == resource_type:
            from . import clinicalimpression

            return clinicalimpression.ClinicalImpression(jsondict, strict)
        if "ClinicalImpressionFinding" == resource_type:
            from . import clinicalimpression

            return clinicalimpression.ClinicalImpressionFinding(jsondict, strict)
        if "ClinicalImpressionInvestigation" == resource_type:
            from . import clinicalimpression

            return clinicalimpression.ClinicalImpressionInvestigation(jsondict, strict)
        if "CodeSystem" == resource_type:
            from . import codesystem

            return codesystem.CodeSystem(jsondict, strict)
        if "CodeSystemConcept" == resource_type:
            from . import codesystem

            return codesystem.CodeSystemConcept(jsondict, strict)
        if "CodeSystemConceptDesignation" == resource_type:
            from . import codesystem

            return codesystem.CodeSystemConceptDesignation(jsondict, strict)
        if "CodeSystemConceptProperty" == resource_type:
            from . import codesystem

            return codesystem.CodeSystemConceptProperty(jsondict, strict)
        if "CodeSystemFilter" == resource_type:
            from . import codesystem

            return codesystem.CodeSystemFilter(jsondict, strict)
        if "CodeSystemProperty" == resource_type:
            from . import codesystem

            return codesystem.CodeSystemProperty(jsondict, strict)
        if "CodeableConcept" == resource_type:
            from . import codeableconcept

            return codeableconcept.CodeableConcept(jsondict, strict)
        if "Coding" == resource_type:
            from . import coding

            return coding.Coding(jsondict, strict)
        if "Communication" == resource_type:
            from . import communication

            return communication.Communication(jsondict, strict)
        if "CommunicationPayload" == resource_type:
            from . import communication

            return communication.CommunicationPayload(jsondict, strict)
        if "CommunicationRequest" == resource_type:
            from . import communicationrequest

            return communicationrequest.CommunicationRequest(jsondict, strict)
        if "CommunicationRequestPayload" == resource_type:
            from . import communicationrequest

            return communicationrequest.CommunicationRequestPayload(jsondict, strict)
        if "CompartmentDefinition" == resource_type:
            from . import compartmentdefinition

            return compartmentdefinition.CompartmentDefinition(jsondict, strict)
        if "CompartmentDefinitionResource" == resource_type:
            from . import compartmentdefinition

            return compartmentdefinition.CompartmentDefinitionResource(jsondict, strict)
        if "Composition" == resource_type:
            from . import composition

            return composition.Composition(jsondict, strict)
        if "CompositionAttester" == resource_type:
            from . import composition

            return composition.CompositionAttester(jsondict, strict)
        if "CompositionEvent" == resource_type:
            from . import composition

            return composition.CompositionEvent(jsondict, strict)
        if "CompositionRelatesTo" == resource_type:
            from . import composition

            return composition.CompositionRelatesTo(jsondict, strict)
        if "CompositionSection" == resource_type:
            from . import composition

            return composition.CompositionSection(jsondict, strict)
        if "ConceptMap" == resource_type:
            from . import conceptmap

            return conceptmap.ConceptMap(jsondict, strict)
        if "ConceptMapGroup" == resource_type:
            from . import conceptmap

            return conceptmap.ConceptMapGroup(jsondict, strict)
        if "ConceptMapGroupElement" == resource_type:
            from . import conceptmap

            return conceptmap.ConceptMapGroupElement(jsondict, strict)
        if "ConceptMapGroupElementTarget" == resource_type:
            from . import conceptmap

            return conceptmap.ConceptMapGroupElementTarget(jsondict, strict)
        if "ConceptMapGroupElementTargetDependsOn" == resource_type:
            from . import conceptmap

            return conceptmap.ConceptMapGroupElementTargetDependsOn(jsondict, strict)
        if "ConceptMapGroupUnmapped" == resource_type:
            from . import conceptmap

            return conceptmap.ConceptMapGroupUnmapped(jsondict, strict)
        if "Condition" == resource_type:
            from . import condition

            return condition.Condition(jsondict, strict)
        if "ConditionEvidence" == resource_type:
            from . import condition

            return condition.ConditionEvidence(jsondict, strict)
        if "ConditionStage" == resource_type:
            from . import condition

            return condition.ConditionStage(jsondict, strict)
        if "Consent" == resource_type:
            from . import consent

            return consent.Consent(jsondict, strict)
        if "ConsentPolicy" == resource_type:
            from . import consent

            return consent.ConsentPolicy(jsondict, strict)
        if "ConsentProvision" == resource_type:
            from . import consent

            return consent.ConsentProvision(jsondict, strict)
        if "ConsentProvisionActor" == resource_type:
            from . import consent

            return consent.ConsentProvisionActor(jsondict, strict)
        if "ConsentProvisionData" == resource_type:
            from . import consent

            return consent.ConsentProvisionData(jsondict, strict)
        if "ConsentVerification" == resource_type:
            from . import consent

            return consent.ConsentVerification(jsondict, strict)
        if "ContactDetail" == resource_type:
            from . import contactdetail

            return contactdetail.ContactDetail(jsondict, strict)
        if "ContactPoint" == resource_type:
            from . import contactpoint

            return contactpoint.ContactPoint(jsondict, strict)
        if "Contract" == resource_type:
            from . import contract

            return contract.Contract(jsondict, strict)
        if "ContractContentDefinition" == resource_type:
            from . import contract

            return contract.ContractContentDefinition(jsondict, strict)
        if "ContractFriendly" == resource_type:
            from . import contract

            return contract.ContractFriendly(jsondict, strict)
        if "ContractLegal" == resource_type:
            from . import contract

            return contract.ContractLegal(jsondict, strict)
        if "ContractRule" == resource_type:
            from . import contract

            return contract.ContractRule(jsondict, strict)
        if "ContractSigner" == resource_type:
            from . import contract

            return contract.ContractSigner(jsondict, strict)
        if "ContractTerm" == resource_type:
            from . import contract

            return contract.ContractTerm(jsondict, strict)
        if "ContractTermAction" == resource_type:
            from . import contract

            return contract.ContractTermAction(jsondict, strict)
        if "ContractTermActionSubject" == resource_type:
            from . import contract

            return contract.ContractTermActionSubject(jsondict, strict)
        if "ContractTermAsset" == resource_type:
            from . import contract

            return contract.ContractTermAsset(jsondict, strict)
        if "ContractTermAssetContext" == resource_type:
            from . import contract

            return contract.ContractTermAssetContext(jsondict, strict)
        if "ContractTermAssetValuedItem" == resource_type:
            from . import contract

            return contract.ContractTermAssetValuedItem(jsondict, strict)
        if "ContractTermOffer" == resource_type:
            from . import contract

            return contract.ContractTermOffer(jsondict, strict)
        if "ContractTermOfferAnswer" == resource_type:
            from . import contract

            return contract.ContractTermOfferAnswer(jsondict, strict)
        if "ContractTermOfferParty" == resource_type:
            from . import contract

            return contract.ContractTermOfferParty(jsondict, strict)
        if "ContractTermSecurityLabel" == resource_type:
            from . import contract

            return contract.ContractTermSecurityLabel(jsondict, strict)
        if "Contributor" == resource_type:
            from . import contributor

            return contributor.Contributor(jsondict, strict)
        if "Count" == resource_type:
            from . import count

            return count.Count(jsondict, strict)
        if "Coverage" == resource_type:
            from . import coverage

            return coverage.Coverage(jsondict, strict)
        if "CoverageClass" == resource_type:
            from . import coverage

            return coverage.CoverageClass(jsondict, strict)
        if "CoverageCostToBeneficiary" == resource_type:
            from . import coverage

            return coverage.CoverageCostToBeneficiary(jsondict, strict)
        if "CoverageCostToBeneficiaryException" == resource_type:
            from . import coverage

            return coverage.CoverageCostToBeneficiaryException(jsondict, strict)
        if "CoverageEligibilityRequest" == resource_type:
            from . import coverageeligibilityrequest

            return coverageeligibilityrequest.CoverageEligibilityRequest(
                jsondict, strict
            )
        if "CoverageEligibilityRequestInsurance" == resource_type:
            from . import coverageeligibilityrequest

            return coverageeligibilityrequest.CoverageEligibilityRequestInsurance(
                jsondict, strict
            )
        if "CoverageEligibilityRequestItem" == resource_type:
            from . import coverageeligibilityrequest

            return coverageeligibilityrequest.CoverageEligibilityRequestItem(
                jsondict, strict
            )
        if "CoverageEligibilityRequestItemDiagnosis" == resource_type:
            from . import coverageeligibilityrequest

            return coverageeligibilityrequest.CoverageEligibilityRequestItemDiagnosis(
                jsondict, strict
            )
        if "CoverageEligibilityRequestSupportingInfo" == resource_type:
            from . import coverageeligibilityrequest

            return coverageeligibilityrequest.CoverageEligibilityRequestSupportingInfo(
                jsondict, strict
            )
        if "CoverageEligibilityResponse" == resource_type:
            from . import coverageeligibilityresponse

            return coverageeligibilityresponse.CoverageEligibilityResponse(
                jsondict, strict
            )
        if "CoverageEligibilityResponseError" == resource_type:
            from . import coverageeligibilityresponse

            return coverageeligibilityresponse.CoverageEligibilityResponseError(
                jsondict, strict
            )
        if "CoverageEligibilityResponseInsurance" == resource_type:
            from . import coverageeligibilityresponse

            return coverageeligibilityresponse.CoverageEligibilityResponseInsurance(
                jsondict, strict
            )
        if "CoverageEligibilityResponseInsuranceItem" == resource_type:
            from . import coverageeligibilityresponse

            return coverageeligibilityresponse.CoverageEligibilityResponseInsuranceItem(
                jsondict, strict
            )
        if "CoverageEligibilityResponseInsuranceItemBenefit" == resource_type:
            from . import coverageeligibilityresponse

            return coverageeligibilityresponse.CoverageEligibilityResponseInsuranceItemBenefit(
                jsondict, strict
            )
        if "DataRequirement" == resource_type:
            from . import datarequirement

            return datarequirement.DataRequirement(jsondict, strict)
        if "DataRequirementCodeFilter" == resource_type:
            from . import datarequirement

            return datarequirement.DataRequirementCodeFilter(jsondict, strict)
        if "DataRequirementDateFilter" == resource_type:
            from . import datarequirement

            return datarequirement.DataRequirementDateFilter(jsondict, strict)
        if "DataRequirementSort" == resource_type:
            from . import datarequirement

            return datarequirement.DataRequirementSort(jsondict, strict)
        if "DetectedIssue" == resource_type:
            from . import detectedissue

            return detectedissue.DetectedIssue(jsondict, strict)
        if "DetectedIssueEvidence" == resource_type:
            from . import detectedissue

            return detectedissue.DetectedIssueEvidence(jsondict, strict)
        if "DetectedIssueMitigation" == resource_type:
            from . import detectedissue

            return detectedissue.DetectedIssueMitigation(jsondict, strict)
        if "Device" == resource_type:
            from . import device

            return device.Device(jsondict, strict)
        if "DeviceDefinition" == resource_type:
            from . import devicedefinition

            return devicedefinition.DeviceDefinition(jsondict, strict)
        if "DeviceDefinitionCapability" == resource_type:
            from . import devicedefinition

            return devicedefinition.DeviceDefinitionCapability(jsondict, strict)
        if "DeviceDefinitionDeviceName" == resource_type:
            from . import devicedefinition

            return devicedefinition.DeviceDefinitionDeviceName(jsondict, strict)
        if "DeviceDefinitionMaterial" == resource_type:
            from . import devicedefinition

            return devicedefinition.DeviceDefinitionMaterial(jsondict, strict)
        if "DeviceDefinitionProperty" == resource_type:
            from . import devicedefinition

            return devicedefinition.DeviceDefinitionProperty(jsondict, strict)
        if "DeviceDefinitionSpecialization" == resource_type:
            from . import devicedefinition

            return devicedefinition.DeviceDefinitionSpecialization(jsondict, strict)
        if "DeviceDefinitionUdiDeviceIdentifier" == resource_type:
            from . import devicedefinition

            return devicedefinition.DeviceDefinitionUdiDeviceIdentifier(
                jsondict, strict
            )
        if "DeviceDeviceName" == resource_type:
            from . import device

            return device.DeviceDeviceName(jsondict, strict)
        if "DeviceMetric" == resource_type:
            from . import devicemetric

            return devicemetric.DeviceMetric(jsondict, strict)
        if "DeviceMetricCalibration" == resource_type:
            from . import devicemetric

            return devicemetric.DeviceMetricCalibration(jsondict, strict)
        if "DeviceProperty" == resource_type:
            from . import device

            return device.DeviceProperty(jsondict, strict)
        if "DeviceRequest" == resource_type:
            from . import devicerequest

            return devicerequest.DeviceRequest(jsondict, strict)
        if "DeviceRequestParameter" == resource_type:
            from . import devicerequest

            return devicerequest.DeviceRequestParameter(jsondict, strict)
        if "DeviceSpecialization" == resource_type:
            from . import device

            return device.DeviceSpecialization(jsondict, strict)
        if "DeviceUdiCarrier" == resource_type:
            from . import device

            return device.DeviceUdiCarrier(jsondict, strict)
        if "DeviceUseStatement" == resource_type:
            from . import deviceusestatement

            return deviceusestatement.DeviceUseStatement(jsondict, strict)
        if "DeviceVersion" == resource_type:
            from . import device

            return device.DeviceVersion(jsondict, strict)
        if "DiagnosticReport" == resource_type:
            from . import diagnosticreport

            return diagnosticreport.DiagnosticReport(jsondict, strict)
        if "DiagnosticReportMedia" == resource_type:
            from . import diagnosticreport

            return diagnosticreport.DiagnosticReportMedia(jsondict, strict)
        if "Distance" == resource_type:
            from . import distance

            return distance.Distance(jsondict, strict)
        if "DocumentManifest" == resource_type:
            from . import documentmanifest

            return documentmanifest.DocumentManifest(jsondict, strict)
        if "DocumentManifestRelated" == resource_type:
            from . import documentmanifest

            return documentmanifest.DocumentManifestRelated(jsondict, strict)
        if "DocumentReference" == resource_type:
            from . import documentreference

            return documentreference.DocumentReference(jsondict, strict)
        if "DocumentReferenceContent" == resource_type:
            from . import documentreference

            return documentreference.DocumentReferenceContent(jsondict, strict)
        if "DocumentReferenceContext" == resource_type:
            from . import documentreference

            return documentreference.DocumentReferenceContext(jsondict, strict)
        if "DocumentReferenceRelatesTo" == resource_type:
            from . import documentreference

            return documentreference.DocumentReferenceRelatesTo(jsondict, strict)
        if "DomainResource" == resource_type:
            from . import domainresource

            return domainresource.DomainResource(jsondict, strict)
        if "Dosage" == resource_type:
            from . import dosage

            return dosage.Dosage(jsondict, strict)
        if "DosageDoseAndRate" == resource_type:
            from . import dosage

            return dosage.DosageDoseAndRate(jsondict, strict)
        if "Duration" == resource_type:
            from . import duration

            return duration.Duration(jsondict, strict)
        if "EffectEvidenceSynthesis" == resource_type:
            from . import effectevidencesynthesis

            return effectevidencesynthesis.EffectEvidenceSynthesis(jsondict, strict)
        if "EffectEvidenceSynthesisCertainty" == resource_type:
            from . import effectevidencesynthesis

            return effectevidencesynthesis.EffectEvidenceSynthesisCertainty(
                jsondict, strict
            )
        if "EffectEvidenceSynthesisCertaintyCertaintySubcomponent" == resource_type:
            from . import effectevidencesynthesis

            return effectevidencesynthesis.EffectEvidenceSynthesisCertaintyCertaintySubcomponent(
                jsondict, strict
            )
        if "EffectEvidenceSynthesisEffectEstimate" == resource_type:
            from . import effectevidencesynthesis

            return effectevidencesynthesis.EffectEvidenceSynthesisEffectEstimate(
                jsondict, strict
            )
        if "EffectEvidenceSynthesisEffectEstimatePrecisionEstimate" == resource_type:
            from . import effectevidencesynthesis

            return effectevidencesynthesis.EffectEvidenceSynthesisEffectEstimatePrecisionEstimate(
                jsondict, strict
            )
        if "EffectEvidenceSynthesisResultsByExposure" == resource_type:
            from . import effectevidencesynthesis

            return effectevidencesynthesis.EffectEvidenceSynthesisResultsByExposure(
                jsondict, strict
            )
        if "EffectEvidenceSynthesisSampleSize" == resource_type:
            from . import effectevidencesynthesis

            return effectevidencesynthesis.EffectEvidenceSynthesisSampleSize(
                jsondict, strict
            )
        if "Element" == resource_type:
            from . import element

            return element.Element(jsondict, strict)
        if "ElementDefinition" == resource_type:
            from . import elementdefinition

            return elementdefinition.ElementDefinition(jsondict, strict)
        if "ElementDefinitionBase" == resource_type:
            from . import elementdefinition

            return elementdefinition.ElementDefinitionBase(jsondict, strict)
        if "ElementDefinitionBinding" == resource_type:
            from . import elementdefinition

            return elementdefinition.ElementDefinitionBinding(jsondict, strict)
        if "ElementDefinitionConstraint" == resource_type:
            from . import elementdefinition

            return elementdefinition.ElementDefinitionConstraint(jsondict, strict)
        if "ElementDefinitionExample" == resource_type:
            from . import elementdefinition

            return elementdefinition.ElementDefinitionExample(jsondict, strict)
        if "ElementDefinitionMapping" == resource_type:
            from . import elementdefinition

            return elementdefinition.ElementDefinitionMapping(jsondict, strict)
        if "ElementDefinitionSlicing" == resource_type:
            from . import elementdefinition

            return elementdefinition.ElementDefinitionSlicing(jsondict, strict)
        if "ElementDefinitionSlicingDiscriminator" == resource_type:
            from . import elementdefinition

            return elementdefinition.ElementDefinitionSlicingDiscriminator(
                jsondict, strict
            )
        if "ElementDefinitionType" == resource_type:
            from . import elementdefinition

            return elementdefinition.ElementDefinitionType(jsondict, strict)
        if "Encounter" == resource_type:
            from . import encounter

            return encounter.Encounter(jsondict, strict)
        if "EncounterClassHistory" == resource_type:
            from . import encounter

            return encounter.EncounterClassHistory(jsondict, strict)
        if "EncounterDiagnosis" == resource_type:
            from . import encounter

            return encounter.EncounterDiagnosis(jsondict, strict)
        if "EncounterHospitalization" == resource_type:
            from . import encounter

            return encounter.EncounterHospitalization(jsondict, strict)
        if "EncounterLocation" == resource_type:
            from . import encounter

            return encounter.EncounterLocation(jsondict, strict)
        if "EncounterParticipant" == resource_type:
            from . import encounter

            return encounter.EncounterParticipant(jsondict, strict)
        if "EncounterStatusHistory" == resource_type:
            from . import encounter

            return encounter.EncounterStatusHistory(jsondict, strict)
        if "Endpoint" == resource_type:
            from . import endpoint

            return endpoint.Endpoint(jsondict, strict)
        if "EnrollmentRequest" == resource_type:
            from . import enrollmentrequest

            return enrollmentrequest.EnrollmentRequest(jsondict, strict)
        if "EnrollmentResponse" == resource_type:
            from . import enrollmentresponse

            return enrollmentresponse.EnrollmentResponse(jsondict, strict)
        if "EpisodeOfCare" == resource_type:
            from . import episodeofcare

            return episodeofcare.EpisodeOfCare(jsondict, strict)
        if "EpisodeOfCareDiagnosis" == resource_type:
            from . import episodeofcare

            return episodeofcare.EpisodeOfCareDiagnosis(jsondict, strict)
        if "EpisodeOfCareStatusHistory" == resource_type:
            from . import episodeofcare

            return episodeofcare.EpisodeOfCareStatusHistory(jsondict, strict)
        if "EventDefinition" == resource_type:
            from . import eventdefinition

            return eventdefinition.EventDefinition(jsondict, strict)
        if "Evidence" == resource_type:
            from . import evidence

            return evidence.Evidence(jsondict, strict)
        if "EvidenceVariable" == resource_type:
            from . import evidencevariable

            return evidencevariable.EvidenceVariable(jsondict, strict)
        if "EvidenceVariableCharacteristic" == resource_type:
            from . import evidencevariable

            return evidencevariable.EvidenceVariableCharacteristic(jsondict, strict)
        if "ExampleScenario" == resource_type:
            from . import examplescenario

            return examplescenario.ExampleScenario(jsondict, strict)
        if "ExampleScenarioActor" == resource_type:
            from . import examplescenario

            return examplescenario.ExampleScenarioActor(jsondict, strict)
        if "ExampleScenarioInstance" == resource_type:
            from . import examplescenario

            return examplescenario.ExampleScenarioInstance(jsondict, strict)
        if "ExampleScenarioInstanceContainedInstance" == resource_type:
            from . import examplescenario

            return examplescenario.ExampleScenarioInstanceContainedInstance(
                jsondict, strict
            )
        if "ExampleScenarioInstanceVersion" == resource_type:
            from . import examplescenario

            return examplescenario.ExampleScenarioInstanceVersion(jsondict, strict)
        if "ExampleScenarioProcess" == resource_type:
            from . import examplescenario

            return examplescenario.ExampleScenarioProcess(jsondict, strict)
        if "ExampleScenarioProcessStep" == resource_type:
            from . import examplescenario

            return examplescenario.ExampleScenarioProcessStep(jsondict, strict)
        if "ExampleScenarioProcessStepAlternative" == resource_type:
            from . import examplescenario

            return examplescenario.ExampleScenarioProcessStepAlternative(
                jsondict, strict
            )
        if "ExampleScenarioProcessStepOperation" == resource_type:
            from . import examplescenario

            return examplescenario.ExampleScenarioProcessStepOperation(jsondict, strict)
        if "ExplanationOfBenefit" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefit(jsondict, strict)
        if "ExplanationOfBenefitAccident" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitAccident(jsondict, strict)
        if "ExplanationOfBenefitAddItem" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitAddItem(jsondict, strict)
        if "ExplanationOfBenefitAddItemDetail" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitAddItemDetail(
                jsondict, strict
            )
        if "ExplanationOfBenefitAddItemDetailSubDetail" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitAddItemDetailSubDetail(
                jsondict, strict
            )
        if "ExplanationOfBenefitBenefitBalance" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitBenefitBalance(
                jsondict, strict
            )
        if "ExplanationOfBenefitBenefitBalanceFinancial" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitBenefitBalanceFinancial(
                jsondict, strict
            )
        if "ExplanationOfBenefitCareTeam" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitCareTeam(jsondict, strict)
        if "ExplanationOfBenefitDiagnosis" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitDiagnosis(jsondict, strict)
        if "ExplanationOfBenefitInsurance" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitInsurance(jsondict, strict)
        if "ExplanationOfBenefitItem" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitItem(jsondict, strict)
        if "ExplanationOfBenefitItemAdjudication" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitItemAdjudication(
                jsondict, strict
            )
        if "ExplanationOfBenefitItemDetail" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitItemDetail(jsondict, strict)
        if "ExplanationOfBenefitItemDetailSubDetail" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitItemDetailSubDetail(
                jsondict, strict
            )
        if "ExplanationOfBenefitPayee" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitPayee(jsondict, strict)
        if "ExplanationOfBenefitPayment" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitPayment(jsondict, strict)
        if "ExplanationOfBenefitProcedure" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitProcedure(jsondict, strict)
        if "ExplanationOfBenefitProcessNote" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitProcessNote(
                jsondict, strict
            )
        if "ExplanationOfBenefitRelated" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitRelated(jsondict, strict)
        if "ExplanationOfBenefitSupportingInfo" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitSupportingInfo(
                jsondict, strict
            )
        if "ExplanationOfBenefitTotal" == resource_type:
            from . import explanationofbenefit

            return explanationofbenefit.ExplanationOfBenefitTotal(jsondict, strict)
        if "Expression" == resource_type:
            from . import expression

            return expression.Expression(jsondict, strict)
        if "Extension" == resource_type:
            from . import extension

            return extension.Extension(jsondict, strict)
        if "FamilyMemberHistory" == resource_type:
            from . import familymemberhistory

            return familymemberhistory.FamilyMemberHistory(jsondict, strict)
        if "FamilyMemberHistoryCondition" == resource_type:
            from . import familymemberhistory

            return familymemberhistory.FamilyMemberHistoryCondition(jsondict, strict)
        if "Flag" == resource_type:
            from . import flag

            return flag.Flag(jsondict, strict)
        if "Goal" == resource_type:
            from . import goal

            return goal.Goal(jsondict, strict)
        if "GoalTarget" == resource_type:
            from . import goal

            return goal.GoalTarget(jsondict, strict)
        if "GraphDefinition" == resource_type:
            from . import graphdefinition

            return graphdefinition.GraphDefinition(jsondict, strict)
        if "GraphDefinitionLink" == resource_type:
            from . import graphdefinition

            return graphdefinition.GraphDefinitionLink(jsondict, strict)
        if "GraphDefinitionLinkTarget" == resource_type:
            from . import graphdefinition

            return graphdefinition.GraphDefinitionLinkTarget(jsondict, strict)
        if "GraphDefinitionLinkTargetCompartment" == resource_type:
            from . import graphdefinition

            return graphdefinition.GraphDefinitionLinkTargetCompartment(
                jsondict, strict
            )
        if "Group" == resource_type:
            from . import group

            return group.Group(jsondict, strict)
        if "GroupCharacteristic" == resource_type:
            from . import group

            return group.GroupCharacteristic(jsondict, strict)
        if "GroupMember" == resource_type:
            from . import group

            return group.GroupMember(jsondict, strict)
        if "GuidanceResponse" == resource_type:
            from . import guidanceresponse

            return guidanceresponse.GuidanceResponse(jsondict, strict)
        if "HealthcareService" == resource_type:
            from . import healthcareservice

            return healthcareservice.HealthcareService(jsondict, strict)
        if "HealthcareServiceAvailableTime" == resource_type:
            from . import healthcareservice

            return healthcareservice.HealthcareServiceAvailableTime(jsondict, strict)
        if "HealthcareServiceEligibility" == resource_type:
            from . import healthcareservice

            return healthcareservice.HealthcareServiceEligibility(jsondict, strict)
        if "HealthcareServiceNotAvailable" == resource_type:
            from . import healthcareservice

            return healthcareservice.HealthcareServiceNotAvailable(jsondict, strict)
        if "HumanName" == resource_type:
            from . import humanname

            return humanname.HumanName(jsondict, strict)
        if "Identifier" == resource_type:
            from . import identifier

            return identifier.Identifier(jsondict, strict)
        if "ImagingStudy" == resource_type:
            from . import imagingstudy

            return imagingstudy.ImagingStudy(jsondict, strict)
        if "ImagingStudySeries" == resource_type:
            from . import imagingstudy

            return imagingstudy.ImagingStudySeries(jsondict, strict)
        if "ImagingStudySeriesInstance" == resource_type:
            from . import imagingstudy

            return imagingstudy.ImagingStudySeriesInstance(jsondict, strict)
        if "ImagingStudySeriesPerformer" == resource_type:
            from . import imagingstudy

            return imagingstudy.ImagingStudySeriesPerformer(jsondict, strict)
        if "Immunization" == resource_type:
            from . import immunization

            return immunization.Immunization(jsondict, strict)
        if "ImmunizationEducation" == resource_type:
            from . import immunization

            return immunization.ImmunizationEducation(jsondict, strict)
        if "ImmunizationEvaluation" == resource_type:
            from . import immunizationevaluation

            return immunizationevaluation.ImmunizationEvaluation(jsondict, strict)
        if "ImmunizationPerformer" == resource_type:
            from . import immunization

            return immunization.ImmunizationPerformer(jsondict, strict)
        if "ImmunizationProtocolApplied" == resource_type:
            from . import immunization

            return immunization.ImmunizationProtocolApplied(jsondict, strict)
        if "ImmunizationReaction" == resource_type:
            from . import immunization

            return immunization.ImmunizationReaction(jsondict, strict)
        if "ImmunizationRecommendation" == resource_type:
            from . import immunizationrecommendation

            return immunizationrecommendation.ImmunizationRecommendation(
                jsondict, strict
            )
        if "ImmunizationRecommendationRecommendation" == resource_type:
            from . import immunizationrecommendation

            return immunizationrecommendation.ImmunizationRecommendationRecommendation(
                jsondict, strict
            )
        if "ImmunizationRecommendationRecommendationDateCriterion" == resource_type:
            from . import immunizationrecommendation

            return immunizationrecommendation.ImmunizationRecommendationRecommendationDateCriterion(
                jsondict, strict
            )
        if "ImplementationGuide" == resource_type:
            from . import implementationguide

            return implementationguide.ImplementationGuide(jsondict, strict)
        if "ImplementationGuideDefinition" == resource_type:
            from . import implementationguide

            return implementationguide.ImplementationGuideDefinition(jsondict, strict)
        if "ImplementationGuideDefinitionGrouping" == resource_type:
            from . import implementationguide

            return implementationguide.ImplementationGuideDefinitionGrouping(
                jsondict, strict
            )
        if "ImplementationGuideDefinitionPage" == resource_type:
            from . import implementationguide

            return implementationguide.ImplementationGuideDefinitionPage(
                jsondict, strict
            )
        if "ImplementationGuideDefinitionParameter" == resource_type:
            from . import implementationguide

            return implementationguide.ImplementationGuideDefinitionParameter(
                jsondict, strict
            )
        if "ImplementationGuideDefinitionResource" == resource_type:
            from . import implementationguide

            return implementationguide.ImplementationGuideDefinitionResource(
                jsondict, strict
            )
        if "ImplementationGuideDefinitionTemplate" == resource_type:
            from . import implementationguide

            return implementationguide.ImplementationGuideDefinitionTemplate(
                jsondict, strict
            )
        if "ImplementationGuideDependsOn" == resource_type:
            from . import implementationguide

            return implementationguide.ImplementationGuideDependsOn(jsondict, strict)
        if "ImplementationGuideGlobal" == resource_type:
            from . import implementationguide

            return implementationguide.ImplementationGuideGlobal(jsondict, strict)
        if "ImplementationGuideManifest" == resource_type:
            from . import implementationguide

            return implementationguide.ImplementationGuideManifest(jsondict, strict)
        if "ImplementationGuideManifestPage" == resource_type:
            from . import implementationguide

            return implementationguide.ImplementationGuideManifestPage(jsondict, strict)
        if "ImplementationGuideManifestResource" == resource_type:
            from . import implementationguide

            return implementationguide.ImplementationGuideManifestResource(
                jsondict, strict
            )
        if "InsurancePlan" == resource_type:
            from . import insuranceplan

            return insuranceplan.InsurancePlan(jsondict, strict)
        if "InsurancePlanContact" == resource_type:
            from . import insuranceplan

            return insuranceplan.InsurancePlanContact(jsondict, strict)
        if "InsurancePlanCoverage" == resource_type:
            from . import insuranceplan

            return insuranceplan.InsurancePlanCoverage(jsondict, strict)
        if "InsurancePlanCoverageBenefit" == resource_type:
            from . import insuranceplan

            return insuranceplan.InsurancePlanCoverageBenefit(jsondict, strict)
        if "InsurancePlanCoverageBenefitLimit" == resource_type:
            from . import insuranceplan

            return insuranceplan.InsurancePlanCoverageBenefitLimit(jsondict, strict)
        if "InsurancePlanPlan" == resource_type:
            from . import insuranceplan

            return insuranceplan.InsurancePlanPlan(jsondict, strict)
        if "InsurancePlanPlanGeneralCost" == resource_type:
            from . import insuranceplan

            return insuranceplan.InsurancePlanPlanGeneralCost(jsondict, strict)
        if "InsurancePlanPlanSpecificCost" == resource_type:
            from . import insuranceplan

            return insuranceplan.InsurancePlanPlanSpecificCost(jsondict, strict)
        if "InsurancePlanPlanSpecificCostBenefit" == resource_type:
            from . import insuranceplan

            return insuranceplan.InsurancePlanPlanSpecificCostBenefit(jsondict, strict)
        if "InsurancePlanPlanSpecificCostBenefitCost" == resource_type:
            from . import insuranceplan

            return insuranceplan.InsurancePlanPlanSpecificCostBenefitCost(
                jsondict, strict
            )
        if "Invoice" == resource_type:
            from . import invoice

            return invoice.Invoice(jsondict, strict)
        if "InvoiceLineItem" == resource_type:
            from . import invoice

            return invoice.InvoiceLineItem(jsondict, strict)
        if "InvoiceLineItemPriceComponent" == resource_type:
            from . import invoice

            return invoice.InvoiceLineItemPriceComponent(jsondict, strict)
        if "InvoiceParticipant" == resource_type:
            from . import invoice

            return invoice.InvoiceParticipant(jsondict, strict)
        if "Library" == resource_type:
            from . import library

            return library.Library(jsondict, strict)
        if "Linkage" == resource_type:
            from . import linkage

            return linkage.Linkage(jsondict, strict)
        if "LinkageItem" == resource_type:
            from . import linkage

            return linkage.LinkageItem(jsondict, strict)
        if "List" == resource_type:
            from . import list

            return list.List(jsondict, strict)
        if "ListEntry" == resource_type:
            from . import list

            return list.ListEntry(jsondict, strict)
        if "Location" == resource_type:
            from . import location

            return location.Location(jsondict, strict)
        if "LocationHoursOfOperation" == resource_type:
            from . import location

            return location.LocationHoursOfOperation(jsondict, strict)
        if "LocationPosition" == resource_type:
            from . import location

            return location.LocationPosition(jsondict, strict)
        if "MarketingStatus" == resource_type:
            from . import marketingstatus

            return marketingstatus.MarketingStatus(jsondict, strict)
        if "Measure" == resource_type:
            from . import measure

            return measure.Measure(jsondict, strict)
        if "MeasureGroup" == resource_type:
            from . import measure

            return measure.MeasureGroup(jsondict, strict)
        if "MeasureGroupPopulation" == resource_type:
            from . import measure

            return measure.MeasureGroupPopulation(jsondict, strict)
        if "MeasureGroupStratifier" == resource_type:
            from . import measure

            return measure.MeasureGroupStratifier(jsondict, strict)
        if "MeasureGroupStratifierComponent" == resource_type:
            from . import measure

            return measure.MeasureGroupStratifierComponent(jsondict, strict)
        if "MeasureReport" == resource_type:
            from . import measurereport

            return measurereport.MeasureReport(jsondict, strict)
        if "MeasureReportGroup" == resource_type:
            from . import measurereport

            return measurereport.MeasureReportGroup(jsondict, strict)
        if "MeasureReportGroupPopulation" == resource_type:
            from . import measurereport

            return measurereport.MeasureReportGroupPopulation(jsondict, strict)
        if "MeasureReportGroupStratifier" == resource_type:
            from . import measurereport

            return measurereport.MeasureReportGroupStratifier(jsondict, strict)
        if "MeasureReportGroupStratifierStratum" == resource_type:
            from . import measurereport

            return measurereport.MeasureReportGroupStratifierStratum(jsondict, strict)
        if "MeasureReportGroupStratifierStratumComponent" == resource_type:
            from . import measurereport

            return measurereport.MeasureReportGroupStratifierStratumComponent(
                jsondict, strict
            )
        if "MeasureReportGroupStratifierStratumPopulation" == resource_type:
            from . import measurereport

            return measurereport.MeasureReportGroupStratifierStratumPopulation(
                jsondict, strict
            )
        if "MeasureSupplementalData" == resource_type:
            from . import measure

            return measure.MeasureSupplementalData(jsondict, strict)
        if "Media" == resource_type:
            from . import media

            return media.Media(jsondict, strict)
        if "Medication" == resource_type:
            from . import medication

            return medication.Medication(jsondict, strict)
        if "MedicationAdministration" == resource_type:
            from . import medicationadministration

            return medicationadministration.MedicationAdministration(jsondict, strict)
        if "MedicationAdministrationDosage" == resource_type:
            from . import medicationadministration

            return medicationadministration.MedicationAdministrationDosage(
                jsondict, strict
            )
        if "MedicationAdministrationPerformer" == resource_type:
            from . import medicationadministration

            return medicationadministration.MedicationAdministrationPerformer(
                jsondict, strict
            )
        if "MedicationBatch" == resource_type:
            from . import medication

            return medication.MedicationBatch(jsondict, strict)
        if "MedicationDispense" == resource_type:
            from . import medicationdispense

            return medicationdispense.MedicationDispense(jsondict, strict)
        if "MedicationDispensePerformer" == resource_type:
            from . import medicationdispense

            return medicationdispense.MedicationDispensePerformer(jsondict, strict)
        if "MedicationDispenseSubstitution" == resource_type:
            from . import medicationdispense

            return medicationdispense.MedicationDispenseSubstitution(jsondict, strict)
        if "MedicationIngredient" == resource_type:
            from . import medication

            return medication.MedicationIngredient(jsondict, strict)
        if "MedicationKnowledge" == resource_type:
            from . import medicationknowledge

            return medicationknowledge.MedicationKnowledge(jsondict, strict)
        if "MedicationKnowledgeAdministrationGuidelines" == resource_type:
            from . import medicationknowledge

            return medicationknowledge.MedicationKnowledgeAdministrationGuidelines(
                jsondict, strict
            )
        if "MedicationKnowledgeAdministrationGuidelinesDosage" == resource_type:
            from . import medicationknowledge

            return medicationknowledge.MedicationKnowledgeAdministrationGuidelinesDosage(
                jsondict, strict
            )
        if (
            "MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics"
            == resource_type
        ):
            from . import medicationknowledge

            return medicationknowledge.MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics(
                jsondict, strict
            )
        if "MedicationKnowledgeCost" == resource_type:
            from . import medicationknowledge

            return medicationknowledge.MedicationKnowledgeCost(jsondict, strict)
        if "MedicationKnowledgeDrugCharacteristic" == resource_type:
            from . import medicationknowledge

            return medicationknowledge.MedicationKnowledgeDrugCharacteristic(
                jsondict, strict
            )
        if "MedicationKnowledgeIngredient" == resource_type:
            from . import medicationknowledge

            return medicationknowledge.MedicationKnowledgeIngredient(jsondict, strict)
        if "MedicationKnowledgeKinetics" == resource_type:
            from . import medicationknowledge

            return medicationknowledge.MedicationKnowledgeKinetics(jsondict, strict)
        if "MedicationKnowledgeMedicineClassification" == resource_type:
            from . import medicationknowledge

            return medicationknowledge.MedicationKnowledgeMedicineClassification(
                jsondict, strict
            )
        if "MedicationKnowledgeMonitoringProgram" == resource_type:
            from . import medicationknowledge

            return medicationknowledge.MedicationKnowledgeMonitoringProgram(
                jsondict, strict
            )
        if "MedicationKnowledgeMonograph" == resource_type:
            from . import medicationknowledge

            return medicationknowledge.MedicationKnowledgeMonograph(jsondict, strict)
        if "MedicationKnowledgePackaging" == resource_type:
            from . import medicationknowledge

            return medicationknowledge.MedicationKnowledgePackaging(jsondict, strict)
        if "MedicationKnowledgeRegulatory" == resource_type:
            from . import medicationknowledge

            return medicationknowledge.MedicationKnowledgeRegulatory(jsondict, strict)
        if "MedicationKnowledgeRegulatoryMaxDispense" == resource_type:
            from . import medicationknowledge

            return medicationknowledge.MedicationKnowledgeRegulatoryMaxDispense(
                jsondict, strict
            )
        if "MedicationKnowledgeRegulatorySchedule" == resource_type:
            from . import medicationknowledge

            return medicationknowledge.MedicationKnowledgeRegulatorySchedule(
                jsondict, strict
            )
        if "MedicationKnowledgeRegulatorySubstitution" == resource_type:
            from . import medicationknowledge

            return medicationknowledge.MedicationKnowledgeRegulatorySubstitution(
                jsondict, strict
            )
        if "MedicationKnowledgeRelatedMedicationKnowledge" == resource_type:
            from . import medicationknowledge

            return medicationknowledge.MedicationKnowledgeRelatedMedicationKnowledge(
                jsondict, strict
            )
        if "MedicationRequest" == resource_type:
            from . import medicationrequest

            return medicationrequest.MedicationRequest(jsondict, strict)
        if "MedicationRequestDispenseRequest" == resource_type:
            from . import medicationrequest

            return medicationrequest.MedicationRequestDispenseRequest(jsondict, strict)
        if "MedicationRequestDispenseRequestInitialFill" == resource_type:
            from . import medicationrequest

            return medicationrequest.MedicationRequestDispenseRequestInitialFill(
                jsondict, strict
            )
        if "MedicationRequestSubstitution" == resource_type:
            from . import medicationrequest

            return medicationrequest.MedicationRequestSubstitution(jsondict, strict)
        if "MedicationStatement" == resource_type:
            from . import medicationstatement

            return medicationstatement.MedicationStatement(jsondict, strict)
        if "MedicinalProduct" == resource_type:
            from . import medicinalproduct

            return medicinalproduct.MedicinalProduct(jsondict, strict)
        if "MedicinalProductAuthorization" == resource_type:
            from . import medicinalproductauthorization

            return medicinalproductauthorization.MedicinalProductAuthorization(
                jsondict, strict
            )
        if "MedicinalProductAuthorizationJurisdictionalAuthorization" == resource_type:
            from . import medicinalproductauthorization

            return medicinalproductauthorization.MedicinalProductAuthorizationJurisdictionalAuthorization(
                jsondict, strict
            )
        if "MedicinalProductAuthorizationProcedure" == resource_type:
            from . import medicinalproductauthorization

            return medicinalproductauthorization.MedicinalProductAuthorizationProcedure(
                jsondict, strict
            )
        if "MedicinalProductContraindication" == resource_type:
            from . import medicinalproductcontraindication

            return medicinalproductcontraindication.MedicinalProductContraindication(
                jsondict, strict
            )
        if "MedicinalProductContraindicationOtherTherapy" == resource_type:
            from . import medicinalproductcontraindication

            return medicinalproductcontraindication.MedicinalProductContraindicationOtherTherapy(
                jsondict, strict
            )
        if "MedicinalProductIndication" == resource_type:
            from . import medicinalproductindication

            return medicinalproductindication.MedicinalProductIndication(
                jsondict, strict
            )
        if "MedicinalProductIndicationOtherTherapy" == resource_type:
            from . import medicinalproductindication

            return medicinalproductindication.MedicinalProductIndicationOtherTherapy(
                jsondict, strict
            )
        if "MedicinalProductIngredient" == resource_type:
            from . import medicinalproductingredient

            return medicinalproductingredient.MedicinalProductIngredient(
                jsondict, strict
            )
        if "MedicinalProductIngredientSpecifiedSubstance" == resource_type:
            from . import medicinalproductingredient

            return medicinalproductingredient.MedicinalProductIngredientSpecifiedSubstance(
                jsondict, strict
            )
        if "MedicinalProductIngredientSpecifiedSubstanceStrength" == resource_type:
            from . import medicinalproductingredient

            return medicinalproductingredient.MedicinalProductIngredientSpecifiedSubstanceStrength(
                jsondict, strict
            )
        if (
            "MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength"
            == resource_type
        ):
            from . import medicinalproductingredient

            return medicinalproductingredient.MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength(
                jsondict, strict
            )
        if "MedicinalProductIngredientSubstance" == resource_type:
            from . import medicinalproductingredient

            return medicinalproductingredient.MedicinalProductIngredientSubstance(
                jsondict, strict
            )
        if "MedicinalProductInteraction" == resource_type:
            from . import medicinalproductinteraction

            return medicinalproductinteraction.MedicinalProductInteraction(
                jsondict, strict
            )
        if "MedicinalProductInteractionInteractant" == resource_type:
            from . import medicinalproductinteraction

            return medicinalproductinteraction.MedicinalProductInteractionInteractant(
                jsondict, strict
            )
        if "MedicinalProductManufactured" == resource_type:
            from . import medicinalproductmanufactured

            return medicinalproductmanufactured.MedicinalProductManufactured(
                jsondict, strict
            )
        if "MedicinalProductManufacturingBusinessOperation" == resource_type:
            from . import medicinalproduct

            return medicinalproduct.MedicinalProductManufacturingBusinessOperation(
                jsondict, strict
            )
        if "MedicinalProductName" == resource_type:
            from . import medicinalproduct

            return medicinalproduct.MedicinalProductName(jsondict, strict)
        if "MedicinalProductNameCountryLanguage" == resource_type:
            from . import medicinalproduct

            return medicinalproduct.MedicinalProductNameCountryLanguage(
                jsondict, strict
            )
        if "MedicinalProductNameNamePart" == resource_type:
            from . import medicinalproduct

            return medicinalproduct.MedicinalProductNameNamePart(jsondict, strict)
        if "MedicinalProductPackaged" == resource_type:
            from . import medicinalproductpackaged

            return medicinalproductpackaged.MedicinalProductPackaged(jsondict, strict)
        if "MedicinalProductPackagedBatchIdentifier" == resource_type:
            from . import medicinalproductpackaged

            return medicinalproductpackaged.MedicinalProductPackagedBatchIdentifier(
                jsondict, strict
            )
        if "MedicinalProductPackagedPackageItem" == resource_type:
            from . import medicinalproductpackaged

            return medicinalproductpackaged.MedicinalProductPackagedPackageItem(
                jsondict, strict
            )
        if "MedicinalProductPharmaceutical" == resource_type:
            from . import medicinalproductpharmaceutical

            return medicinalproductpharmaceutical.MedicinalProductPharmaceutical(
                jsondict, strict
            )
        if "MedicinalProductPharmaceuticalCharacteristics" == resource_type:
            from . import medicinalproductpharmaceutical

            return medicinalproductpharmaceutical.MedicinalProductPharmaceuticalCharacteristics(
                jsondict, strict
            )
        if "MedicinalProductPharmaceuticalRouteOfAdministration" == resource_type:
            from . import medicinalproductpharmaceutical

            return medicinalproductpharmaceutical.MedicinalProductPharmaceuticalRouteOfAdministration(
                jsondict, strict
            )
        if (
            "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies"
            == resource_type
        ):
            from . import medicinalproductpharmaceutical

            return medicinalproductpharmaceutical.MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies(
                jsondict, strict
            )
        if (
            "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod"
            == resource_type
        ):
            from . import medicinalproductpharmaceutical

            return medicinalproductpharmaceutical.MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod(
                jsondict, strict
            )
        if "MedicinalProductSpecialDesignation" == resource_type:
            from . import medicinalproduct

            return medicinalproduct.MedicinalProductSpecialDesignation(jsondict, strict)
        if "MedicinalProductUndesirableEffect" == resource_type:
            from . import medicinalproductundesirableeffect

            return medicinalproductundesirableeffect.MedicinalProductUndesirableEffect(
                jsondict, strict
            )
        if "MessageDefinition" == resource_type:
            from . import messagedefinition

            return messagedefinition.MessageDefinition(jsondict, strict)
        if "MessageDefinitionAllowedResponse" == resource_type:
            from . import messagedefinition

            return messagedefinition.MessageDefinitionAllowedResponse(jsondict, strict)
        if "MessageDefinitionFocus" == resource_type:
            from . import messagedefinition

            return messagedefinition.MessageDefinitionFocus(jsondict, strict)
        if "MessageHeader" == resource_type:
            from . import messageheader

            return messageheader.MessageHeader(jsondict, strict)
        if "MessageHeaderDestination" == resource_type:
            from . import messageheader

            return messageheader.MessageHeaderDestination(jsondict, strict)
        if "MessageHeaderResponse" == resource_type:
            from . import messageheader

            return messageheader.MessageHeaderResponse(jsondict, strict)
        if "MessageHeaderSource" == resource_type:
            from . import messageheader

            return messageheader.MessageHeaderSource(jsondict, strict)
        if "Meta" == resource_type:
            from . import meta

            return meta.Meta(jsondict, strict)
        if "MetadataResource" == resource_type:
            from . import metadataresource

            return metadataresource.MetadataResource(jsondict, strict)
        if "MolecularSequence" == resource_type:
            from . import molecularsequence

            return molecularsequence.MolecularSequence(jsondict, strict)
        if "MolecularSequenceQuality" == resource_type:
            from . import molecularsequence

            return molecularsequence.MolecularSequenceQuality(jsondict, strict)
        if "MolecularSequenceQualityRoc" == resource_type:
            from . import molecularsequence

            return molecularsequence.MolecularSequenceQualityRoc(jsondict, strict)
        if "MolecularSequenceReferenceSeq" == resource_type:
            from . import molecularsequence

            return molecularsequence.MolecularSequenceReferenceSeq(jsondict, strict)
        if "MolecularSequenceRepository" == resource_type:
            from . import molecularsequence

            return molecularsequence.MolecularSequenceRepository(jsondict, strict)
        if "MolecularSequenceStructureVariant" == resource_type:
            from . import molecularsequence

            return molecularsequence.MolecularSequenceStructureVariant(jsondict, strict)
        if "MolecularSequenceStructureVariantInner" == resource_type:
            from . import molecularsequence

            return molecularsequence.MolecularSequenceStructureVariantInner(
                jsondict, strict
            )
        if "MolecularSequenceStructureVariantOuter" == resource_type:
            from . import molecularsequence

            return molecularsequence.MolecularSequenceStructureVariantOuter(
                jsondict, strict
            )
        if "MolecularSequenceVariant" == resource_type:
            from . import molecularsequence

            return molecularsequence.MolecularSequenceVariant(jsondict, strict)
        if "Money" == resource_type:
            from . import money

            return money.Money(jsondict, strict)
        if "NamingSystem" == resource_type:
            from . import namingsystem

            return namingsystem.NamingSystem(jsondict, strict)
        if "NamingSystemUniqueId" == resource_type:
            from . import namingsystem

            return namingsystem.NamingSystemUniqueId(jsondict, strict)
        if "Narrative" == resource_type:
            from . import narrative

            return narrative.Narrative(jsondict, strict)
        if "NutritionOrder" == resource_type:
            from . import nutritionorder

            return nutritionorder.NutritionOrder(jsondict, strict)
        if "NutritionOrderEnteralFormula" == resource_type:
            from . import nutritionorder

            return nutritionorder.NutritionOrderEnteralFormula(jsondict, strict)
        if "NutritionOrderEnteralFormulaAdministration" == resource_type:
            from . import nutritionorder

            return nutritionorder.NutritionOrderEnteralFormulaAdministration(
                jsondict, strict
            )
        if "NutritionOrderOralDiet" == resource_type:
            from . import nutritionorder

            return nutritionorder.NutritionOrderOralDiet(jsondict, strict)
        if "NutritionOrderOralDietNutrient" == resource_type:
            from . import nutritionorder

            return nutritionorder.NutritionOrderOralDietNutrient(jsondict, strict)
        if "NutritionOrderOralDietTexture" == resource_type:
            from . import nutritionorder

            return nutritionorder.NutritionOrderOralDietTexture(jsondict, strict)
        if "NutritionOrderSupplement" == resource_type:
            from . import nutritionorder

            return nutritionorder.NutritionOrderSupplement(jsondict, strict)
        if "Observation" == resource_type:
            from . import observation

            return observation.Observation(jsondict, strict)
        if "ObservationComponent" == resource_type:
            from . import observation

            return observation.ObservationComponent(jsondict, strict)
        if "ObservationDefinition" == resource_type:
            from . import observationdefinition

            return observationdefinition.ObservationDefinition(jsondict, strict)
        if "ObservationDefinitionQualifiedInterval" == resource_type:
            from . import observationdefinition

            return observationdefinition.ObservationDefinitionQualifiedInterval(
                jsondict, strict
            )
        if "ObservationDefinitionQuantitativeDetails" == resource_type:
            from . import observationdefinition

            return observationdefinition.ObservationDefinitionQuantitativeDetails(
                jsondict, strict
            )
        if "ObservationReferenceRange" == resource_type:
            from . import observation

            return observation.ObservationReferenceRange(jsondict, strict)
        if "OperationDefinition" == resource_type:
            from . import operationdefinition

            return operationdefinition.OperationDefinition(jsondict, strict)
        if "OperationDefinitionOverload" == resource_type:
            from . import operationdefinition

            return operationdefinition.OperationDefinitionOverload(jsondict, strict)
        if "OperationDefinitionParameter" == resource_type:
            from . import operationdefinition

            return operationdefinition.OperationDefinitionParameter(jsondict, strict)
        if "OperationDefinitionParameterBinding" == resource_type:
            from . import operationdefinition

            return operationdefinition.OperationDefinitionParameterBinding(
                jsondict, strict
            )
        if "OperationDefinitionParameterReferencedFrom" == resource_type:
            from . import operationdefinition

            return operationdefinition.OperationDefinitionParameterReferencedFrom(
                jsondict, strict
            )
        if "OperationOutcome" == resource_type:
            from . import operationoutcome

            return operationoutcome.OperationOutcome(jsondict, strict)
        if "OperationOutcomeIssue" == resource_type:
            from . import operationoutcome

            return operationoutcome.OperationOutcomeIssue(jsondict, strict)
        if "Organization" == resource_type:
            from . import organization

            return organization.Organization(jsondict, strict)
        if "OrganizationAffiliation" == resource_type:
            from . import organizationaffiliation

            return organizationaffiliation.OrganizationAffiliation(jsondict, strict)
        if "OrganizationContact" == resource_type:
            from . import organization

            return organization.OrganizationContact(jsondict, strict)
        if "ParameterDefinition" == resource_type:
            from . import parameterdefinition

            return parameterdefinition.ParameterDefinition(jsondict, strict)
        if "Parameters" == resource_type:
            from . import parameters

            return parameters.Parameters(jsondict, strict)
        if "ParametersParameter" == resource_type:
            from . import parameters

            return parameters.ParametersParameter(jsondict, strict)
        if "Patient" == resource_type:
            from . import patient

            return patient.Patient(jsondict, strict)
        if "PatientCommunication" == resource_type:
            from . import patient

            return patient.PatientCommunication(jsondict, strict)
        if "PatientContact" == resource_type:
            from . import patient

            return patient.PatientContact(jsondict, strict)
        if "PatientLink" == resource_type:
            from . import patient

            return patient.PatientLink(jsondict, strict)
        if "PaymentNotice" == resource_type:
            from . import paymentnotice

            return paymentnotice.PaymentNotice(jsondict, strict)
        if "PaymentReconciliation" == resource_type:
            from . import paymentreconciliation

            return paymentreconciliation.PaymentReconciliation(jsondict, strict)
        if "PaymentReconciliationDetail" == resource_type:
            from . import paymentreconciliation

            return paymentreconciliation.PaymentReconciliationDetail(jsondict, strict)
        if "PaymentReconciliationProcessNote" == resource_type:
            from . import paymentreconciliation

            return paymentreconciliation.PaymentReconciliationProcessNote(
                jsondict, strict
            )
        if "Period" == resource_type:
            from . import period

            return period.Period(jsondict, strict)
        if "Person" == resource_type:
            from . import person

            return person.Person(jsondict, strict)
        if "PersonLink" == resource_type:
            from . import person

            return person.PersonLink(jsondict, strict)
        if "PlanDefinition" == resource_type:
            from . import plandefinition

            return plandefinition.PlanDefinition(jsondict, strict)
        if "PlanDefinitionAction" == resource_type:
            from . import plandefinition

            return plandefinition.PlanDefinitionAction(jsondict, strict)
        if "PlanDefinitionActionCondition" == resource_type:
            from . import plandefinition

            return plandefinition.PlanDefinitionActionCondition(jsondict, strict)
        if "PlanDefinitionActionDynamicValue" == resource_type:
            from . import plandefinition

            return plandefinition.PlanDefinitionActionDynamicValue(jsondict, strict)
        if "PlanDefinitionActionParticipant" == resource_type:
            from . import plandefinition

            return plandefinition.PlanDefinitionActionParticipant(jsondict, strict)
        if "PlanDefinitionActionRelatedAction" == resource_type:
            from . import plandefinition

            return plandefinition.PlanDefinitionActionRelatedAction(jsondict, strict)
        if "PlanDefinitionGoal" == resource_type:
            from . import plandefinition

            return plandefinition.PlanDefinitionGoal(jsondict, strict)
        if "PlanDefinitionGoalTarget" == resource_type:
            from . import plandefinition

            return plandefinition.PlanDefinitionGoalTarget(jsondict, strict)
        if "Population" == resource_type:
            from . import population

            return population.Population(jsondict, strict)
        if "Practitioner" == resource_type:
            from . import practitioner

            return practitioner.Practitioner(jsondict, strict)
        if "PractitionerQualification" == resource_type:
            from . import practitioner

            return practitioner.PractitionerQualification(jsondict, strict)
        if "PractitionerRole" == resource_type:
            from . import practitionerrole

            return practitionerrole.PractitionerRole(jsondict, strict)
        if "PractitionerRoleAvailableTime" == resource_type:
            from . import practitionerrole

            return practitionerrole.PractitionerRoleAvailableTime(jsondict, strict)
        if "PractitionerRoleNotAvailable" == resource_type:
            from . import practitionerrole

            return practitionerrole.PractitionerRoleNotAvailable(jsondict, strict)
        if "Procedure" == resource_type:
            from . import procedure

            return procedure.Procedure(jsondict, strict)
        if "ProcedureFocalDevice" == resource_type:
            from . import procedure

            return procedure.ProcedureFocalDevice(jsondict, strict)
        if "ProcedurePerformer" == resource_type:
            from . import procedure

            return procedure.ProcedurePerformer(jsondict, strict)
        if "ProdCharacteristic" == resource_type:
            from . import prodcharacteristic

            return prodcharacteristic.ProdCharacteristic(jsondict, strict)
        if "ProductShelfLife" == resource_type:
            from . import productshelflife

            return productshelflife.ProductShelfLife(jsondict, strict)
        if "Provenance" == resource_type:
            from . import provenance

            return provenance.Provenance(jsondict, strict)
        if "ProvenanceAgent" == resource_type:
            from . import provenance

            return provenance.ProvenanceAgent(jsondict, strict)
        if "ProvenanceEntity" == resource_type:
            from . import provenance

            return provenance.ProvenanceEntity(jsondict, strict)
        if "Quantity" == resource_type:
            from . import quantity

            return quantity.Quantity(jsondict, strict)
        if "Quantity" == resource_type:
            from . import quantity

            return quantity.Quantity(jsondict, strict)
        if "Questionnaire" == resource_type:
            from . import questionnaire

            return questionnaire.Questionnaire(jsondict, strict)
        if "QuestionnaireItem" == resource_type:
            from . import questionnaire

            return questionnaire.QuestionnaireItem(jsondict, strict)
        if "QuestionnaireItemAnswerOption" == resource_type:
            from . import questionnaire

            return questionnaire.QuestionnaireItemAnswerOption(jsondict, strict)
        if "QuestionnaireItemEnableWhen" == resource_type:
            from . import questionnaire

            return questionnaire.QuestionnaireItemEnableWhen(jsondict, strict)
        if "QuestionnaireItemInitial" == resource_type:
            from . import questionnaire

            return questionnaire.QuestionnaireItemInitial(jsondict, strict)
        if "QuestionnaireResponse" == resource_type:
            from . import questionnaireresponse

            return questionnaireresponse.QuestionnaireResponse(jsondict, strict)
        if "QuestionnaireResponseItem" == resource_type:
            from . import questionnaireresponse

            return questionnaireresponse.QuestionnaireResponseItem(jsondict, strict)
        if "QuestionnaireResponseItemAnswer" == resource_type:
            from . import questionnaireresponse

            return questionnaireresponse.QuestionnaireResponseItemAnswer(
                jsondict, strict
            )
        if "Range" == resource_type:
            from . import range

            return range.Range(jsondict, strict)
        if "Ratio" == resource_type:
            from . import ratio

            return ratio.Ratio(jsondict, strict)
        if "Reference" == resource_type:
            from . import reference

            return reference.Reference(jsondict, strict)
        if "RelatedArtifact" == resource_type:
            from . import relatedartifact

            return relatedartifact.RelatedArtifact(jsondict, strict)
        if "RelatedPerson" == resource_type:
            from . import relatedperson

            return relatedperson.RelatedPerson(jsondict, strict)
        if "RelatedPersonCommunication" == resource_type:
            from . import relatedperson

            return relatedperson.RelatedPersonCommunication(jsondict, strict)
        if "RequestGroup" == resource_type:
            from . import requestgroup

            return requestgroup.RequestGroup(jsondict, strict)
        if "RequestGroupAction" == resource_type:
            from . import requestgroup

            return requestgroup.RequestGroupAction(jsondict, strict)
        if "RequestGroupActionCondition" == resource_type:
            from . import requestgroup

            return requestgroup.RequestGroupActionCondition(jsondict, strict)
        if "RequestGroupActionRelatedAction" == resource_type:
            from . import requestgroup

            return requestgroup.RequestGroupActionRelatedAction(jsondict, strict)
        if "ResearchDefinition" == resource_type:
            from . import researchdefinition

            return researchdefinition.ResearchDefinition(jsondict, strict)
        if "ResearchElementDefinition" == resource_type:
            from . import researchelementdefinition

            return researchelementdefinition.ResearchElementDefinition(jsondict, strict)
        if "ResearchElementDefinitionCharacteristic" == resource_type:
            from . import researchelementdefinition

            return researchelementdefinition.ResearchElementDefinitionCharacteristic(
                jsondict, strict
            )
        if "ResearchStudy" == resource_type:
            from . import researchstudy

            return researchstudy.ResearchStudy(jsondict, strict)
        if "ResearchStudyArm" == resource_type:
            from . import researchstudy

            return researchstudy.ResearchStudyArm(jsondict, strict)
        if "ResearchStudyObjective" == resource_type:
            from . import researchstudy

            return researchstudy.ResearchStudyObjective(jsondict, strict)
        if "ResearchSubject" == resource_type:
            from . import researchsubject

            return researchsubject.ResearchSubject(jsondict, strict)
        if "Resource" == resource_type:
            from . import resource

            return resource.Resource(jsondict, strict)
        if "RiskAssessment" == resource_type:
            from . import riskassessment

            return riskassessment.RiskAssessment(jsondict, strict)
        if "RiskAssessmentPrediction" == resource_type:
            from . import riskassessment

            return riskassessment.RiskAssessmentPrediction(jsondict, strict)
        if "RiskEvidenceSynthesis" == resource_type:
            from . import riskevidencesynthesis

            return riskevidencesynthesis.RiskEvidenceSynthesis(jsondict, strict)
        if "RiskEvidenceSynthesisCertainty" == resource_type:
            from . import riskevidencesynthesis

            return riskevidencesynthesis.RiskEvidenceSynthesisCertainty(
                jsondict, strict
            )
        if "RiskEvidenceSynthesisCertaintyCertaintySubcomponent" == resource_type:
            from . import riskevidencesynthesis

            return riskevidencesynthesis.RiskEvidenceSynthesisCertaintyCertaintySubcomponent(
                jsondict, strict
            )
        if "RiskEvidenceSynthesisRiskEstimate" == resource_type:
            from . import riskevidencesynthesis

            return riskevidencesynthesis.RiskEvidenceSynthesisRiskEstimate(
                jsondict, strict
            )
        if "RiskEvidenceSynthesisRiskEstimatePrecisionEstimate" == resource_type:
            from . import riskevidencesynthesis

            return riskevidencesynthesis.RiskEvidenceSynthesisRiskEstimatePrecisionEstimate(
                jsondict, strict
            )
        if "RiskEvidenceSynthesisSampleSize" == resource_type:
            from . import riskevidencesynthesis

            return riskevidencesynthesis.RiskEvidenceSynthesisSampleSize(
                jsondict, strict
            )
        if "SampledData" == resource_type:
            from . import sampleddata

            return sampleddata.SampledData(jsondict, strict)
        if "Schedule" == resource_type:
            from . import schedule

            return schedule.Schedule(jsondict, strict)
        if "SearchParameter" == resource_type:
            from . import searchparameter

            return searchparameter.SearchParameter(jsondict, strict)
        if "SearchParameterComponent" == resource_type:
            from . import searchparameter

            return searchparameter.SearchParameterComponent(jsondict, strict)
        if "ServiceRequest" == resource_type:
            from . import servicerequest

            return servicerequest.ServiceRequest(jsondict, strict)
        if "Signature" == resource_type:
            from . import signature

            return signature.Signature(jsondict, strict)
        if "Slot" == resource_type:
            from . import slot

            return slot.Slot(jsondict, strict)
        if "Specimen" == resource_type:
            from . import specimen

            return specimen.Specimen(jsondict, strict)
        if "SpecimenCollection" == resource_type:
            from . import specimen

            return specimen.SpecimenCollection(jsondict, strict)
        if "SpecimenContainer" == resource_type:
            from . import specimen

            return specimen.SpecimenContainer(jsondict, strict)
        if "SpecimenDefinition" == resource_type:
            from . import specimendefinition

            return specimendefinition.SpecimenDefinition(jsondict, strict)
        if "SpecimenDefinitionTypeTested" == resource_type:
            from . import specimendefinition

            return specimendefinition.SpecimenDefinitionTypeTested(jsondict, strict)
        if "SpecimenDefinitionTypeTestedContainer" == resource_type:
            from . import specimendefinition

            return specimendefinition.SpecimenDefinitionTypeTestedContainer(
                jsondict, strict
            )
        if "SpecimenDefinitionTypeTestedContainerAdditive" == resource_type:
            from . import specimendefinition

            return specimendefinition.SpecimenDefinitionTypeTestedContainerAdditive(
                jsondict, strict
            )
        if "SpecimenDefinitionTypeTestedHandling" == resource_type:
            from . import specimendefinition

            return specimendefinition.SpecimenDefinitionTypeTestedHandling(
                jsondict, strict
            )
        if "SpecimenProcessing" == resource_type:
            from . import specimen

            return specimen.SpecimenProcessing(jsondict, strict)
        if "StructureDefinition" == resource_type:
            from . import structuredefinition

            return structuredefinition.StructureDefinition(jsondict, strict)
        if "StructureDefinitionContext" == resource_type:
            from . import structuredefinition

            return structuredefinition.StructureDefinitionContext(jsondict, strict)
        if "StructureDefinitionDifferential" == resource_type:
            from . import structuredefinition

            return structuredefinition.StructureDefinitionDifferential(jsondict, strict)
        if "StructureDefinitionMapping" == resource_type:
            from . import structuredefinition

            return structuredefinition.StructureDefinitionMapping(jsondict, strict)
        if "StructureDefinitionSnapshot" == resource_type:
            from . import structuredefinition

            return structuredefinition.StructureDefinitionSnapshot(jsondict, strict)
        if "StructureMap" == resource_type:
            from . import structuremap

            return structuremap.StructureMap(jsondict, strict)
        if "StructureMapGroup" == resource_type:
            from . import structuremap

            return structuremap.StructureMapGroup(jsondict, strict)
        if "StructureMapGroupInput" == resource_type:
            from . import structuremap

            return structuremap.StructureMapGroupInput(jsondict, strict)
        if "StructureMapGroupRule" == resource_type:
            from . import structuremap

            return structuremap.StructureMapGroupRule(jsondict, strict)
        if "StructureMapGroupRuleDependent" == resource_type:
            from . import structuremap

            return structuremap.StructureMapGroupRuleDependent(jsondict, strict)
        if "StructureMapGroupRuleSource" == resource_type:
            from . import structuremap

            return structuremap.StructureMapGroupRuleSource(jsondict, strict)
        if "StructureMapGroupRuleTarget" == resource_type:
            from . import structuremap

            return structuremap.StructureMapGroupRuleTarget(jsondict, strict)
        if "StructureMapGroupRuleTargetParameter" == resource_type:
            from . import structuremap

            return structuremap.StructureMapGroupRuleTargetParameter(jsondict, strict)
        if "StructureMapStructure" == resource_type:
            from . import structuremap

            return structuremap.StructureMapStructure(jsondict, strict)
        if "Subscription" == resource_type:
            from . import subscription

            return subscription.Subscription(jsondict, strict)
        if "SubscriptionChannel" == resource_type:
            from . import subscription

            return subscription.SubscriptionChannel(jsondict, strict)
        if "Substance" == resource_type:
            from . import substance

            return substance.Substance(jsondict, strict)
        if "SubstanceAmount" == resource_type:
            from . import substanceamount

            return substanceamount.SubstanceAmount(jsondict, strict)
        if "SubstanceAmountReferenceRange" == resource_type:
            from . import substanceamount

            return substanceamount.SubstanceAmountReferenceRange(jsondict, strict)
        if "SubstanceIngredient" == resource_type:
            from . import substance

            return substance.SubstanceIngredient(jsondict, strict)
        if "SubstanceInstance" == resource_type:
            from . import substance

            return substance.SubstanceInstance(jsondict, strict)
        if "SubstanceNucleicAcid" == resource_type:
            from . import substancenucleicacid

            return substancenucleicacid.SubstanceNucleicAcid(jsondict, strict)
        if "SubstanceNucleicAcidSubunit" == resource_type:
            from . import substancenucleicacid

            return substancenucleicacid.SubstanceNucleicAcidSubunit(jsondict, strict)
        if "SubstanceNucleicAcidSubunitLinkage" == resource_type:
            from . import substancenucleicacid

            return substancenucleicacid.SubstanceNucleicAcidSubunitLinkage(
                jsondict, strict
            )
        if "SubstanceNucleicAcidSubunitSugar" == resource_type:
            from . import substancenucleicacid

            return substancenucleicacid.SubstanceNucleicAcidSubunitSugar(
                jsondict, strict
            )
        if "SubstancePolymer" == resource_type:
            from . import substancepolymer

            return substancepolymer.SubstancePolymer(jsondict, strict)
        if "SubstancePolymerMonomerSet" == resource_type:
            from . import substancepolymer

            return substancepolymer.SubstancePolymerMonomerSet(jsondict, strict)
        if "SubstancePolymerMonomerSetStartingMaterial" == resource_type:
            from . import substancepolymer

            return substancepolymer.SubstancePolymerMonomerSetStartingMaterial(
                jsondict, strict
            )
        if "SubstancePolymerRepeat" == resource_type:
            from . import substancepolymer

            return substancepolymer.SubstancePolymerRepeat(jsondict, strict)
        if "SubstancePolymerRepeatRepeatUnit" == resource_type:
            from . import substancepolymer

            return substancepolymer.SubstancePolymerRepeatRepeatUnit(jsondict, strict)
        if "SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation" == resource_type:
            from . import substancepolymer

            return substancepolymer.SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation(
                jsondict, strict
            )
        if "SubstancePolymerRepeatRepeatUnitStructuralRepresentation" == resource_type:
            from . import substancepolymer

            return substancepolymer.SubstancePolymerRepeatRepeatUnitStructuralRepresentation(
                jsondict, strict
            )
        if "SubstanceProtein" == resource_type:
            from . import substanceprotein

            return substanceprotein.SubstanceProtein(jsondict, strict)
        if "SubstanceProteinSubunit" == resource_type:
            from . import substanceprotein

            return substanceprotein.SubstanceProteinSubunit(jsondict, strict)
        if "SubstanceReferenceInformation" == resource_type:
            from . import substancereferenceinformation

            return substancereferenceinformation.SubstanceReferenceInformation(
                jsondict, strict
            )
        if "SubstanceReferenceInformationClassification" == resource_type:
            from . import substancereferenceinformation

            return substancereferenceinformation.SubstanceReferenceInformationClassification(
                jsondict, strict
            )
        if "SubstanceReferenceInformationGene" == resource_type:
            from . import substancereferenceinformation

            return substancereferenceinformation.SubstanceReferenceInformationGene(
                jsondict, strict
            )
        if "SubstanceReferenceInformationGeneElement" == resource_type:
            from . import substancereferenceinformation

            return substancereferenceinformation.SubstanceReferenceInformationGeneElement(
                jsondict, strict
            )
        if "SubstanceReferenceInformationTarget" == resource_type:
            from . import substancereferenceinformation

            return substancereferenceinformation.SubstanceReferenceInformationTarget(
                jsondict, strict
            )
        if "SubstanceSourceMaterial" == resource_type:
            from . import substancesourcematerial

            return substancesourcematerial.SubstanceSourceMaterial(jsondict, strict)
        if "SubstanceSourceMaterialFractionDescription" == resource_type:
            from . import substancesourcematerial

            return substancesourcematerial.SubstanceSourceMaterialFractionDescription(
                jsondict, strict
            )
        if "SubstanceSourceMaterialOrganism" == resource_type:
            from . import substancesourcematerial

            return substancesourcematerial.SubstanceSourceMaterialOrganism(
                jsondict, strict
            )
        if "SubstanceSourceMaterialOrganismAuthor" == resource_type:
            from . import substancesourcematerial

            return substancesourcematerial.SubstanceSourceMaterialOrganismAuthor(
                jsondict, strict
            )
        if "SubstanceSourceMaterialOrganismHybrid" == resource_type:
            from . import substancesourcematerial

            return substancesourcematerial.SubstanceSourceMaterialOrganismHybrid(
                jsondict, strict
            )
        if "SubstanceSourceMaterialOrganismOrganismGeneral" == resource_type:
            from . import substancesourcematerial

            return substancesourcematerial.SubstanceSourceMaterialOrganismOrganismGeneral(
                jsondict, strict
            )
        if "SubstanceSourceMaterialPartDescription" == resource_type:
            from . import substancesourcematerial

            return substancesourcematerial.SubstanceSourceMaterialPartDescription(
                jsondict, strict
            )
        if "SubstanceSpecification" == resource_type:
            from . import substancespecification

            return substancespecification.SubstanceSpecification(jsondict, strict)
        if "SubstanceSpecificationMoiety" == resource_type:
            from . import substancespecification

            return substancespecification.SubstanceSpecificationMoiety(jsondict, strict)
        if "SubstanceSpecificationName" == resource_type:
            from . import substancespecification

            return substancespecification.SubstanceSpecificationName(jsondict, strict)
        if "SubstanceSpecificationNameOfficial" == resource_type:
            from . import substancespecification

            return substancespecification.SubstanceSpecificationNameOfficial(
                jsondict, strict
            )
        if "SubstanceSpecificationProperty" == resource_type:
            from . import substancespecification

            return substancespecification.SubstanceSpecificationProperty(
                jsondict, strict
            )
        if "SubstanceSpecificationRelationship" == resource_type:
            from . import substancespecification

            return substancespecification.SubstanceSpecificationRelationship(
                jsondict, strict
            )
        if "SubstanceSpecificationStructure" == resource_type:
            from . import substancespecification

            return substancespecification.SubstanceSpecificationStructure(
                jsondict, strict
            )
        if "SubstanceSpecificationStructureIsotope" == resource_type:
            from . import substancespecification

            return substancespecification.SubstanceSpecificationStructureIsotope(
                jsondict, strict
            )
        if "SubstanceSpecificationStructureIsotopeMolecularWeight" == resource_type:
            from . import substancespecification

            return substancespecification.SubstanceSpecificationStructureIsotopeMolecularWeight(
                jsondict, strict
            )
        if "SubstanceSpecificationStructureRepresentation" == resource_type:
            from . import substancespecification

            return substancespecification.SubstanceSpecificationStructureRepresentation(
                jsondict, strict
            )
        if "SubstanceSpecificationstr" == resource_type:
            from . import substancespecification

            return substancespecification.SubstanceSpecificationstr(jsondict, strict)
        if "SupplyDelivery" == resource_type:
            from . import supplydelivery

            return supplydelivery.SupplyDelivery(jsondict, strict)
        if "SupplyDeliverySuppliedItem" == resource_type:
            from . import supplydelivery

            return supplydelivery.SupplyDeliverySuppliedItem(jsondict, strict)
        if "SupplyRequest" == resource_type:
            from . import supplyrequest

            return supplyrequest.SupplyRequest(jsondict, strict)
        if "SupplyRequestParameter" == resource_type:
            from . import supplyrequest

            return supplyrequest.SupplyRequestParameter(jsondict, strict)
        if "Task" == resource_type:
            from . import task

            return task.Task(jsondict, strict)
        if "TaskInput" == resource_type:
            from . import task

            return task.TaskInput(jsondict, strict)
        if "TaskOutput" == resource_type:
            from . import task

            return task.TaskOutput(jsondict, strict)
        if "TaskRestriction" == resource_type:
            from . import task

            return task.TaskRestriction(jsondict, strict)
        if "TerminologyCapabilities" == resource_type:
            from . import terminologycapabilities

            return terminologycapabilities.TerminologyCapabilities(jsondict, strict)
        if "TerminologyCapabilitiesClosure" == resource_type:
            from . import terminologycapabilities

            return terminologycapabilities.TerminologyCapabilitiesClosure(
                jsondict, strict
            )
        if "TerminologyCapabilitiesCodeSystem" == resource_type:
            from . import terminologycapabilities

            return terminologycapabilities.TerminologyCapabilitiesCodeSystem(
                jsondict, strict
            )
        if "TerminologyCapabilitiesCodeSystemVersion" == resource_type:
            from . import terminologycapabilities

            return terminologycapabilities.TerminologyCapabilitiesCodeSystemVersion(
                jsondict, strict
            )
        if "TerminologyCapabilitiesCodeSystemVersionFilter" == resource_type:
            from . import terminologycapabilities

            return terminologycapabilities.TerminologyCapabilitiesCodeSystemVersionFilter(
                jsondict, strict
            )
        if "TerminologyCapabilitiesExpansion" == resource_type:
            from . import terminologycapabilities

            return terminologycapabilities.TerminologyCapabilitiesExpansion(
                jsondict, strict
            )
        if "TerminologyCapabilitiesExpansionParameter" == resource_type:
            from . import terminologycapabilities

            return terminologycapabilities.TerminologyCapabilitiesExpansionParameter(
                jsondict, strict
            )
        if "TerminologyCapabilitiesImplementation" == resource_type:
            from . import terminologycapabilities

            return terminologycapabilities.TerminologyCapabilitiesImplementation(
                jsondict, strict
            )
        if "TerminologyCapabilitiesSoftware" == resource_type:
            from . import terminologycapabilities

            return terminologycapabilities.TerminologyCapabilitiesSoftware(
                jsondict, strict
            )
        if "TerminologyCapabilitiesTranslation" == resource_type:
            from . import terminologycapabilities

            return terminologycapabilities.TerminologyCapabilitiesTranslation(
                jsondict, strict
            )
        if "TerminologyCapabilitiesValidateCode" == resource_type:
            from . import terminologycapabilities

            return terminologycapabilities.TerminologyCapabilitiesValidateCode(
                jsondict, strict
            )
        if "TestReport" == resource_type:
            from . import testreport

            return testreport.TestReport(jsondict, strict)
        if "TestReportParticipant" == resource_type:
            from . import testreport

            return testreport.TestReportParticipant(jsondict, strict)
        if "TestReportSetup" == resource_type:
            from . import testreport

            return testreport.TestReportSetup(jsondict, strict)
        if "TestReportSetupAction" == resource_type:
            from . import testreport

            return testreport.TestReportSetupAction(jsondict, strict)
        if "TestReportSetupActionAssert" == resource_type:
            from . import testreport

            return testreport.TestReportSetupActionAssert(jsondict, strict)
        if "TestReportSetupActionOperation" == resource_type:
            from . import testreport

            return testreport.TestReportSetupActionOperation(jsondict, strict)
        if "TestReportTeardown" == resource_type:
            from . import testreport

            return testreport.TestReportTeardown(jsondict, strict)
        if "TestReportTeardownAction" == resource_type:
            from . import testreport

            return testreport.TestReportTeardownAction(jsondict, strict)
        if "TestReportTest" == resource_type:
            from . import testreport

            return testreport.TestReportTest(jsondict, strict)
        if "TestReportTestAction" == resource_type:
            from . import testreport

            return testreport.TestReportTestAction(jsondict, strict)
        if "TestScript" == resource_type:
            from . import testscript

            return testscript.TestScript(jsondict, strict)
        if "TestScriptDestination" == resource_type:
            from . import testscript

            return testscript.TestScriptDestination(jsondict, strict)
        if "TestScriptFixture" == resource_type:
            from . import testscript

            return testscript.TestScriptFixture(jsondict, strict)
        if "TestScriptMetadata" == resource_type:
            from . import testscript

            return testscript.TestScriptMetadata(jsondict, strict)
        if "TestScriptMetadataCapability" == resource_type:
            from . import testscript

            return testscript.TestScriptMetadataCapability(jsondict, strict)
        if "TestScriptMetadataLink" == resource_type:
            from . import testscript

            return testscript.TestScriptMetadataLink(jsondict, strict)
        if "TestScriptOrigin" == resource_type:
            from . import testscript

            return testscript.TestScriptOrigin(jsondict, strict)
        if "TestScriptSetup" == resource_type:
            from . import testscript

            return testscript.TestScriptSetup(jsondict, strict)
        if "TestScriptSetupAction" == resource_type:
            from . import testscript

            return testscript.TestScriptSetupAction(jsondict, strict)
        if "TestScriptSetupActionAssert" == resource_type:
            from . import testscript

            return testscript.TestScriptSetupActionAssert(jsondict, strict)
        if "TestScriptSetupActionOperation" == resource_type:
            from . import testscript

            return testscript.TestScriptSetupActionOperation(jsondict, strict)
        if "TestScriptSetupActionOperationRequestHeader" == resource_type:
            from . import testscript

            return testscript.TestScriptSetupActionOperationRequestHeader(
                jsondict, strict
            )
        if "TestScriptTeardown" == resource_type:
            from . import testscript

            return testscript.TestScriptTeardown(jsondict, strict)
        if "TestScriptTeardownAction" == resource_type:
            from . import testscript

            return testscript.TestScriptTeardownAction(jsondict, strict)
        if "TestScriptTest" == resource_type:
            from . import testscript

            return testscript.TestScriptTest(jsondict, strict)
        if "TestScriptTestAction" == resource_type:
            from . import testscript

            return testscript.TestScriptTestAction(jsondict, strict)
        if "TestScriptVariable" == resource_type:
            from . import testscript

            return testscript.TestScriptVariable(jsondict, strict)
        if "Timing" == resource_type:
            from . import timing

            return timing.Timing(jsondict, strict)
        if "TimingRepeat" == resource_type:
            from . import timing

            return timing.TimingRepeat(jsondict, strict)
        if "TriggerDefinition" == resource_type:
            from . import triggerdefinition

            return triggerdefinition.TriggerDefinition(jsondict, strict)
        if "UsageContext" == resource_type:
            from . import usagecontext

            return usagecontext.UsageContext(jsondict, strict)
        if "ValueSet" == resource_type:
            from . import valueset

            return valueset.ValueSet(jsondict, strict)
        if "ValueSetCompose" == resource_type:
            from . import valueset

            return valueset.ValueSetCompose(jsondict, strict)
        if "ValueSetComposeInclude" == resource_type:
            from . import valueset

            return valueset.ValueSetComposeInclude(jsondict, strict)
        if "ValueSetComposeIncludeConcept" == resource_type:
            from . import valueset

            return valueset.ValueSetComposeIncludeConcept(jsondict, strict)
        if "ValueSetComposeIncludeConceptDesignation" == resource_type:
            from . import valueset

            return valueset.ValueSetComposeIncludeConceptDesignation(jsondict, strict)
        if "ValueSetComposeIncludeFilter" == resource_type:
            from . import valueset

            return valueset.ValueSetComposeIncludeFilter(jsondict, strict)
        if "ValueSetExpansion" == resource_type:
            from . import valueset

            return valueset.ValueSetExpansion(jsondict, strict)
        if "ValueSetExpansionContains" == resource_type:
            from . import valueset

            return valueset.ValueSetExpansionContains(jsondict, strict)
        if "ValueSetExpansionParameter" == resource_type:
            from . import valueset

            return valueset.ValueSetExpansionParameter(jsondict, strict)
        if "VerificationResult" == resource_type:
            from . import verificationresult

            return verificationresult.VerificationResult(jsondict, strict)
        if "VerificationResultAttestation" == resource_type:
            from . import verificationresult

            return verificationresult.VerificationResultAttestation(jsondict, strict)
        if "VerificationResultPrimarySource" == resource_type:
            from . import verificationresult

            return verificationresult.VerificationResultPrimarySource(jsondict, strict)
        if "VerificationResultValidator" == resource_type:
            from . import verificationresult

            return verificationresult.VerificationResultValidator(jsondict, strict)
        if "VisionPrescription" == resource_type:
            from . import visionprescription

            return visionprescription.VisionPrescription(jsondict, strict)
        if "VisionPrescriptionLensSpecification" == resource_type:
            from . import visionprescription

            return visionprescription.VisionPrescriptionLensSpecification(
                jsondict, strict
            )
        if "VisionPrescriptionLensSpecificationPrism" == resource_type:
            from . import visionprescription

            return visionprescription.VisionPrescriptionLensSpecificationPrism(
                jsondict, strict
            )
        from . import element

        return element.Element(jsondict, strict)
